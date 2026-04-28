from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

data = load_wine()
X = data.data
y = data.target

max_depth = int(input("Enter the max depth of the tree: "))

split_ratios = [0.30, 0.40, 0.25]
split_names = ["70-30", "60-40", "75-25"]
final_results = []

for i in range(len(split_ratios)):
    print("\n--------------------------------------------")
    print("Split:", split_names[i])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=split_ratios[i], random_state=42
    )
    print("Train samples:", len(X_train))
    print("Test samples :", len(X_test))

    dt = DecisionTreeClassifier(max_depth=max_depth, criterion='gini', random_state=42)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print("              Predicted 0   Predicted 1   Predicted 2")
    for idx, row in enumerate(cm):
        print(f"Actual {idx}        {row[0]:5}         {row[1]:5}         {row[2]:5}")

    accuracy  = round(accuracy_score(y_test, y_pred), 4)
    precision = round(precision_score(y_test, y_pred, average='weighted'), 4)
    recall    = round(recall_score(y_test, y_pred, average='weighted'), 4)
    f1        = round(f1_score(y_test, y_pred, average='weighted'), 4)

    print("\nAccuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    final_results.append([split_names[i], accuracy, precision, recall, f1])

print("\n\nFinal Consolidated Results:")
print("Split   Accuracy  Precision    Recall   F1-Score")
for row in final_results:
    print(f"{row[0]:6}   {row[1]:8}   {row[2]:8}   {row[3]:8}   {row[4]:8}")