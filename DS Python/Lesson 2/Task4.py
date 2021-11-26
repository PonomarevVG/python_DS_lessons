#*Задание 4
#В этом задании мы будем работать с датасетом, в котором приведены данные по мошенничеству с кредитными данными:
# Credit Card Fraud Detection (информация об авторах: Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and
# Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on
# Computational Intelligence and Data Mining (CIDM), IEEE, 2015).
#Ознакомьтесь с описанием и скачайте датасет creditcard.csv с сайта Kaggle.com по ссылке:
#Credit Card Fraud Detection
#Данный датасет является примером несбалансированных данных, так как мошеннические операции с картами встречаются
# реже обычных.
#Импортируйте библиотеку Pandas, а также используйте для графиков стиль “fivethirtyeight”.
#Посчитайте с помощью метода value_counts количество наблюдений для каждого значения целевой переменной Class и
# примените к полученным данным метод plot, чтобы построить столбчатую диаграмму. Затем постройте такую же диаграмму,
# используя логарифмический масштаб.
#На следующем графике постройте две гистограммы по значениям признака V1 - одну для мошеннических транзакций
# (Class равен 1) и другую - для обычных (Class равен 0). Подберите значение аргумента density так, чтобы по вертикали
# графика было расположено не число наблюдений, а плотность распределения. Число бинов должно равняться 20 для обеих
# гистограмм, а коэффициент alpha сделайте равным 0.5, чтобы гистограммы были полупрозрачными и не загораживали друг
# друга. Создайте легенду с двумя значениями: “Class 0” и “Class 1”. Гистограмма обычных транзакций должна быть серого
# цвета, а мошеннических - красного. Горизонтальной оси дайте название “V1”.


import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("creditcard.csv")
fraud_stat = data["Class"].value_counts()

fraud_stat.plot(kind="bar")
plt.title("Линейный масштаб")
plt.show()

fraud_stat.plot(kind="bar", logy=True)
plt.title("Логарифмический масштаб")
plt.show()

frauds = data.loc[(data["Class"] == 1), "V1"]
not_frauds = data.loc[(data["Class"] == 0), "V1"]
plt.hist(frauds, density=0.5, alpha=0.5, bins=20, color="grey", label="Class 1")
plt.hist(not_frauds, density=0.5, alpha=0.5, bins=20, color="red", label="Class 0")
plt.xlabel("V1")
plt.legend()
plt.show()
