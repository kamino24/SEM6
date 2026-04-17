import os
import math
import random
import csv
from collections import Counter

def distance_metric(p1, p2, choice):
    dim = len(p1)
    if choice == '1':  # Euclidean
        return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(dim)))
    elif choice == '2':  # Manhattan
        return sum(abs(p1[i] - p2[i]) for i in range(dim))
    else:
        # Default to Euclidean
        return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(dim)))

def normalisation(data, choice):
    if not data:
        return [], None

    num_features = len(data[0]) - 1  # Last column is the class

    if choice == '1':  # Min-Max Normalization
        mins = [min(d[i] for d in data) for i in range(num_features)]
        maxs = [max(d[i] for d in data) for i in range(num_features)]
        params = (mins, maxs)

        norm = []
        for row in data:
            features = [
                (row[i]-mins[i])/(maxs[i]-mins[i]) if (maxs[i]-mins[i]) != 0 else 0
                for i in range(num_features)
            ]
            norm.append(features + [row[num_features]])
        return norm, params

    elif choice == '2':  # Z-Score Normalization
        means = [sum(d[i] for d in data)/len(data) for i in range(num_features)]
        stds = [
            math.sqrt(sum((d[i]-means[i])**2 for d in data)/len(data))
            for i in range(num_features)
        ]
        params = (means, stds)

        norm = []
        for row in data:
            features = [
                (row[i]-means[i])/stds[i] if stds[i] != 0 else 0
                for i in range(num_features)
            ]
            norm.append(features + [row[num_features]])
        return norm, params

    return data, None
def balance_data(data):
    # Separate the classes
    class_0 = [row for row in data if int(row[-1]) == 0]
    class_1 = [row for row in data if int(row[-1]) == 1]

    #print(f"\nBefore balancing: Class 0 = {len(class_0)}, Class 1 = {len(class_1)}")

    # Find which one is smaller
    min_size = min(len(class_0), len(class_1))

    # Sample both to the same size
    balanced_0 = random.sample(class_0, min_size)
    balanced_1 = random.sample(class_1, min_size)

    combined = balanced_0 + balanced_1
    random.shuffle(combined) # Shuffle so they aren't grouped

    #print(f"After balancing: {len(combined)} total samples ({min_size} per class)")
    return combined

def normalize_point(point, params, choice):
    if not params:
        return point

    new_point = []
    if choice == '1': # Min-Max
        mins, maxs = params
        for i in range(len(point)):
            denom = maxs[i] - mins[i]
            val = (point[i] - mins[i]) / denom if denom != 0 else 0
            new_point.append(val)

    elif choice == '2': # Z-Score
        means, stds = params
        for i in range(len(point)):
            val = (point[i] - means[i]) / stds[i] if stds[i] != 0 else 0
            new_point.append(val)

    return new_point

def read_csv(file):
    data = []
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                try:
                    float_row = [float(value) for value in r]
                    data.append(float_row)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Error: File not found.")
    return data

def knn_process(data, unknown, dist_choice):
    table = []
    num_features = len(data[0]) - 1

    for row in data:
        dist = distance_metric(row[:num_features], unknown, dist_choice)
        table.append(row[:num_features] + [dist, row[num_features]])

    table.sort(key=lambda r: r[num_features])

    return table

def print_table(table, k=None):
    num_features = len(table[0]) - 2

    header = f"{'Features':<35} {'Dist':<10} {'Rank':<5} {'Class':<5}"

    print("\n" + header)
    print("-" * (len(header) + 5))

    for i, r in enumerate(table):
        if k is not None and i >= k:
            continue

        dist_val = r[num_features]
        class_val = r[num_features + 1]

        feats = " ".join([f"{x:6.2f}" for x in r[:num_features]])

        row_str = f"{feats}  {dist_val:10.2f} \t{i+1:<5} {int(class_val):<5}"
        print(row_str)

def predict(neighbors, mode, num_features):
    class_index = num_features + 1
    dist_index = num_features

    if mode == 'U':
        votes = Counter([n[class_index] for n in neighbors])
        print("\nUnweighted votes:", dict(votes))
        return votes.most_common(1)[0][0]

    weights = {}
    for n in neighbors:
        dist = n[dist_index]
        cls = n[class_index]
        w = 1 / (dist + 1e-5)
        weights[cls] = weights.get(cls, 0) + w

    print("\nFinal Weighted values:")
    for c, w in weights.items():
        print(f"Class {int(c)} : {w:.6f}")

    return max(weights, key=weights.get)

LOAN_DESC = """
==================================================
DATASET DESCRIPTION: Loan Default Prediction
==================================================
Goal: Predict if a borrower will fail to repay.

FEATURES:
1. Age         : Applicant's age (numeric)
2. Income      : Annual gross income (numeric)
3. LoanAmount  : Total principal requested (numeric)
4. CreditScore : Creditworthiness rating (numeric)
5. Employment  : Months at current job (numeric)

LABELS (Target):
0 : Repaid successfully (Non-Default)
1 : Failed to repay (Default)
==================================================
"""

def main():
    data = read_csv("loan_default.csv")
    print(LOAN_DESC)
    data = balance_data(data)
    if not data:
        print("No data loaded. Exiting.")
        return

    if len(data) >= 20:
        try:
            a = int(input("Enter number of data you need: "))
            data = random.sample(data, a)
        except ValueError:
            print("Invalid input for data sample size.")
            return

    norm_params = None
    norm_choice = None

    norm_apply = input("Apply normalization? (Y/N): ").upper()
    if norm_apply == 'Y':
        print("\n--- Normalization Menu ---")
        print("1. Min-Max")
        print("2. Z-Score")
        norm_choice = input("Enter choice (1 or 2): ")
        data, norm_params = normalisation(data, norm_choice)

    print("\n--- Distance Metric Menu ---")
    print("1. Euclidean")
    print("2. Manhattan")
    dist_choice = input("Enter choice (1 or 2): ")

    print("\nEnter unknown point features (space separated): ")
    try:
        unknown = list(map(float, input().split()))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    if norm_apply == 'Y' and norm_params:
        unknown = normalize_point(unknown, norm_params, norm_choice)
        print(f"\nNormalized unknown point: {[round(x, 4) for x in unknown]}")

    sorted_table = knn_process(data, unknown, dist_choice)
    print_table(sorted_table, k=None)

    try:
        k = int(input("\nEnter value of k: "))
    except ValueError:
        print("Invalid k.")
        return
    print(f"\n--- Neighbors Table (k={k}) ---")
    print_table(sorted_table, k=k)

    #mode = input("\nWeighted or Unweighted (W/U): ").upper()
    result1 = predict(sorted_table[:k], 'W', len(data[0]) - 1)
    #print("\nPredicted class from Weighted:", int(result))
    result2 = predict(sorted_table[:k], 'U', len(data[0]) - 1)
    print("-"*7)
    print("\t\tWeighted\tUnweighted\n")
    print("Predicted Class\t",int(result1),"\t\t",int(result2))

if __name__ == "__main__":
    main()