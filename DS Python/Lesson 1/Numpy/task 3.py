import numpy as np

a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
mean_a = a.mean(axis=0)

a_centered = a - mean_a

a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])
print(f"Скалярное произведение столбцов  столбцов массива a_centered ={a_centered_sp}")
N = a[:,0].size
print(f"Число наблюдений (N) = {N}")
print(f"a_centered_sp / N-1 = {a_centered_sp / (N - 1)}")