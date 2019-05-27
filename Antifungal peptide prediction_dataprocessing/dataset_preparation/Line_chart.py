# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
train_errors = []
test_errors = []
validation_errors = []
axis_x = []
with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\logs\Results_f5.log") as log1:
    for line in log1:
        if line[-1] == "\n":
            line = line[0:-1]
            line = line.split()
            if len(line) >= 1:
                if line[0] == "train_NErrors=":
                    train_errors.append(line[2])
                if line[0] == "test_NErrors=":
                    test_errors.append(line[2])
                if line[0] == "validation_NErrors=":
                    validation_errors.append(line[2])
for i in range(50):
    axis_x.append(i)
print(train_errors)
print(test_errors)
print(validation_errors)
print(axis_x)

train_errors1 = []
test_errors1 = []
validation_errors1 = []
axis_x1 = []
for value in train_errors:
    train_errors1.append(float(value))
train_errors = train_errors1
for value in test_errors:
    test_errors1.append(float(value))
test_errors = test_errors1
for value in validation_errors:
    validation_errors1.append(float(value))
validation_errors = validation_errors1
for value in axis_x:
    axis_x1.append(float(value))
axis_x = axis_x1


# plt.figure(figsize=(8,4))
plt.plot(axis_x, train_errors, label="$train-errors$", color="red", linewidth=1)
plt.plot(axis_x, test_errors, label="$test-errors$", color="green", linewidth=1)
plt.plot(axis_x, validation_errors, label="$validation-errors$", color="skyblue", linewidth=1)
plt.xlabel("Epochs(every 10)")
plt.ylabel("errors(%)")
plt.title("fold_5 line chart")
plt.ylim(0, 100)
plt.legend()
plt.show()
