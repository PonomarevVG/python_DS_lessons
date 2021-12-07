# *Задание 3
# Вызовите документацию для класса RandomForestRegressor,
# найдите информацию об атрибуте feature_importances_.
# С помощью этого атрибута найдите сумму всех показателей важности,
# установите, какие два признака показывают наибольшую важность.

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
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

print(f"Сумма Атрибутов feature_importances_= {model.feature_importances_.sum()}")

sortex_id = model.feature_importances_.argsort()

print(f"Наибольшее влияние оказывают {feature_names[sortex_id[-1]]} и {feature_names[sortex_id[-2]]}")
plt.barh(feature_names[sortex_id], model.feature_importances_[sortex_id])
plt.xlabel("Важность")
plt.ylabel("Атрибуте feature_importances_")
plt.show()
# Как мы видим из графика, наибольшее влияние оказывают RM и LS_stat
