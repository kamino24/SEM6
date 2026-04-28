import math
from collections import Counter

# --- [Existing Data Reading & Entropy Logic] ---

def read_data(filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().strip().split("\n")
            headers = [h.strip() for h in lines[0].split(",")]
            data = [ [v.strip() for v in line.split(",")] for line in lines[1:]]
        return headers, data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit()

def entropy(data):
    if not data: return 0, Counter()
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    ent = sum([-(count/total) * math.log2(count/total) for count in counts.values()])
    return ent, counts

def split_data(data, attribute_index, value):
    return [row for row in data if row[attribute_index] == value]

def information_gain(data, attribute_index):
    parent_entropy, _ = entropy(data)
    total = len(data)
    values = sorted(list(set(row[attribute_index] for row in data)))
    weighted_entropy = 0
    for value in values:
        subset = split_data(data, attribute_index, value)
        sub_ent, _ = entropy(subset)
        weighted_entropy += (len(subset) / total) * sub_ent
    return parent_entropy - weighted_entropy

# --- [New Recursive Logic for Full Tree] ---

def build_tree(data, headers, attributes):
    labels = [row[-1] for row in data]

    # If all records have the same label, return that label
    if len(set(labels)) == 1:
        return labels[0]

    # If no attributes left to split, return the most common label
    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    # Find the best attribute to split on
    best_gain = -1
    best_attr_index = -1

    for attr_index in attributes:
        gain = information_gain(data, attr_index)
        if gain > best_gain:
            best_gain = gain
            best_attr_index = attr_index

    best_attr_name = headers[best_attr_index]
    tree = {best_attr_name: {}}

    # Remaining attributes to pass down
    remaining_attrs = [i for i in attributes if i != best_attr_index]

    # Split data for each value of the best attribute
    attr_values = sorted(list(set(row[best_attr_index] for row in data)))
    for val in attr_values:
        subset = split_data(data, best_attr_index, val)
        tree[best_attr_name][val] = build_tree(subset, headers, remaining_attrs)

    return tree

def print_tree(tree, indent=""):
    """Recursively prints the dictionary-based tree in a readable format"""
    if not isinstance(tree, dict):
        print(f" -> RESULT: {tree}")
        return

    for attribute, branches in tree.items():
        for value, subtree in branches.items():
            print(f"{indent}[{attribute} == {value}]", end="")
            if isinstance(subtree, dict):
                print()
                print_tree(subtree, indent + "    ")
            else:
                print(f" -> {subtree}")

# --- [Modified Find Root to keep flow clean] ---

def find_root_node(data, headers, attributes_dict):
    # This just kicks off the recursive building
    attr_indices = list(attributes_dict.values())
    print("\n" + "="*60)
    print("BUILDING FULL DECISION TREE")
    print("="*60)

    full_tree = build_tree(data, headers, attr_indices)

    print("\nFINAL TREE STRUCTURE:")
    print("-" * 30)
    print_tree(full_tree)
    print("-" * 30)
    return full_tree

if __name__ == "__main__":
    filename_input = input("Enter dataset filename (e.g., data): ")
    if not filename_input.endswith(".txt"):
        filename_input += ".txt"

    headers, data = read_data(filename_input)
    attributes_dict = {headers[i]: i for i in range(len(headers)-1)}

    find_root_node(data, headers, attributes_dict)