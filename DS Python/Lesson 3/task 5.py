# *Дополнительные задания:
# 1). Загрузите датасет Wine из встроенных датасетов sklearn.datasets с помощью функции load_wine в переменную data.
from sklearn.datasets import load_wine
import pandas as pd
data = load_wine()

# 2). Полученный датасет не является датафреймом. Это структура данных, имеющая ключи аналогично словарю.
# Просмотрите тип данных этой структуры данных и создайте список data_keys, содержащий ее ключи.
data_keys = data.keys()
print("\nЗадание 2")
print(data_keys)

# 3). Просмотрите данные, описание и названия признаков в датасете. Описание нужно вывести в виде привычного,
# аккуратно оформленного текста, без обозначений переноса строки, но с самими переносами и т.д.
print("\nЗадание 3")
feature_names = data["feature_names"]
print("feature_names: ")
for el in feature_names:
    print(el)

print(f"\nDESCR:\n {data['DESCR']}")

# 4) Сколько классов содержит целевая переменная датасета? Выведите названия классов.
y = pd.DataFrame(data["target"], columns=["target"])
classes = pd.unique(y['target'])
print("\nЗадание 4")
print(f"Число классов вин = {len(classes)}, существующие классы: {classes}")

# 5). На основе данных датасета (они содержатся в двумерном массиве Numpy) и названий признаков создайте датафрейм
# под названием X.
X = pd.DataFrame(data["data"], columns=feature_names)
print("\nЗадание 5")
print(X)

# 6). Выясните размер датафрейма X и установите, имеются ли в нем пропущенные значения.
print("\nЗадание 6")
print(X.info())

# 7). Добавьте в датафрейм поле с классами вин в виде чисел, имеющих тип данных numpy.int64. Название поля - 'target'.
print("\nЗадание 7")
X["target"] = y
print(X)

# 8). Постройте матрицу корреляций для всех полей X. Дайте полученному датафрейму название X_corr.
print("\nЗадание 8")
X_corr = X.corr()
print(X_corr)

# 9). Создайте список high_corr из признаков, корреляция которых с полем target по абсолютному значению превышает 0.5
# (причем, само поле target не должно входить в этот список).
print("\nЗадание 9")
high_corr = [
    feature_name
    for feature_name, val in zip(feature_names, X_corr["target"])
    if abs(val) > 0.5
]
print(f"high_corr = {high_corr}")

# 10). Удалите из датафрейма X поле с целевой переменной. Для всех признаков, названия которых содержатся в списке
# high_corr, вычислите квадрат их значений и добавьте в датафрейм X соответствующие поля с суффиксом '_2',
# добавленного к первоначальному названию признака. Итоговый датафрейм должен содержать все поля, которые,
# были в нем изначально, а также поля с признаками из списка high_corr, возведенными в квадрат.
# Выведите описание полей датафрейма X с помощью метода describe.
print("\nЗадание 10")
X.drop("target", axis=1, inplace=True)
print(X)
for feature_name in high_corr:
    X[feature_name+"_2"] = X[feature_name] ** 2
pd.options.display.max_columns = 100
print(X)
pd.options.display.max_columns = 0
print(f"Description: \n {X.describe()}")
