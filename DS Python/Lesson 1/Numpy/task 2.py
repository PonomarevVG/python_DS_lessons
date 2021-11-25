import numpy as np

a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
mean_a = a.mean(axis=0)

a_centered = a - mean_a
print("a_centered =")
print(a_centered)