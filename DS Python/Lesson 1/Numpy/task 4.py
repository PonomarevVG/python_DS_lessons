import numpy as np

a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
a_cov = np.cov(a.T)
print("Ковариационная матрицв = ")
print(a_cov)
print(f"Ковариация = {a_cov[0, 1]}")