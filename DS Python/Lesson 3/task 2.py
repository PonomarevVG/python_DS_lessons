# Задание 2
# Создайте модель под названием model с помощью RandomForestRegressor из модуля sklearn.ensemble.
# Сделайте агрумент n_estimators равным 1000,
# max_depth должен быть равен 12 и random_state сделайте равным 42.
# Обучите модель на тренировочных данных аналогично тому, как вы обучали модель LinearRegression,
# но при этом в метод fit вместо датафрейма y_train поставьте y_train.values[:, 0],
# чтобы получить из датафрейма одномерный массив Numpy,
# так как для класса RandomForestRegressor в данном методе для аргумента y предпочтительно применение массивов
# вместо датафрейма.
# Сделайте предсказание на тестовых данных и посчитайте R2. Сравните с результатом из предыдущего задания.
# Напишите в комментариях к коду, какая модель в данном случае работает лучше.

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import warnings

warnings.filterwarnings('ignore')

boston = load_boston()

data = boston["data"]

feature_names = boston["feature_names"]

target = boston["target"]

X = pd.DataFrame(data, columns=feature_names)
y = pd.DataFrame(target, columns=["price"])

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.3, random_state=42)
model = RandomForestRegressor(max_depth=12, n_estimators=1000)

model.fit(X_train, y_train.values[:, 0])

y_pred = model.predict(X_valid)

check_test = pd.DataFrame({
    "Реальное значение": y_valid["price"],
    "Предсказанное значение": y_pred.flatten()
})

print(f"Метрика R2 = {r2_score(y_valid, y_pred)}")

# LinearRegression: Метрика R2 = 0.70074741801493
# RandomForestRegressor: Метрика R2 = 0.829170095416174
# На основе метрики R2, мы видим, что RandomForestRegressor эффективнее в случае решения данной задачи


