def activation(yin):
    if yin > 0.0:
        return 1
    else:
        return 0
'''    if yin > 0.0:
        return 1
    else:
        return -1'''

def train():
    global w, b
    max_epochs = 5
    for epoch in range(1, max_epochs + 1):
        print("\n===== Epoch", epoch, "=====")
        print("Inputs\t t\t yin\t y\t weights\t\t b")
        print("----------------------------------------------------------------")
        error = False
        for row in data:
            x = row[:-1]
            t = row[-1]

            yin = b
            for i in range(n):
                yin += x[i] * w[i]

            y = activation(yin)

            if y != t:
                for i in range(n):
                    w[i] = w[i] + alpha * x[i] * t
                b = b + alpha * t
                error = True

            w_str = "[" + ", ".join(f"{wi:.2f}" for wi in w) + "]"

            print("{:<10} {:<5} {:<8} {:<5} {:<15} {:<5}".format(
                str(x),
                t,
                f"{yin:.2f}",
                y,
                w_str,
                f"{b:.2f}"
            ))

        print("----------------------------------------------------------------")
        w_str = "[" + ", ".join(f"{wi:.2f}" for wi in w) + "]"
        print("Updated weights:", w_str, "b =", f"{b:.2f}")

        if not error:
            print("\nConverged at Epoch", epoch)
            return

    print("\nStopped at max epoch (5)")

data = []
with open("data.txt", "r") as f:
    for line in f:
        row = list(map(int, line.split()))
        data.append(row)

n = int(input("Enter number of inputs (n): "))
w = []
print("Enter initial weights:")
for i in range(n):
    w.append(float(input(f"w{i+1}: ")))
b = float(input("Enter bias (b): "))
alpha = float(input("Enter learning rate (alpha): "))

#print("\nSelect Activation Function:")
#print("1. Binary (0,1)")
print("Bipolar inputs: (-1,1)")
#activation_type = int(input("Enter choice (1 or 2): "))

train()

print("\nFinal Answer:")
print("Weights:", [round(wi, 2) for wi in w], "Bias:", round(b, 2))