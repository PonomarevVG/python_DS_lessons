# *Задание 3
# Примените модель KMeans, построенную в предыдущем задании,
# к данным из тестового набора.
# Вычислите средние значения price и CRIM в разных кластерах на тестовых данных.

import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings('ignore')

boston = load_boston()

X = pd.DataFrame(boston["data"], columns=boston["feature_names"])
y = pd.DataFrame(boston["target"], columns=["price"])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mmscaler = MinMaxScaler()
X_train_scaled = pd.DataFrame(mmscaler.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(mmscaler.transform(X_test), columns=X_test.columns)


model = KMeans(n_clusters=3, max_iter=100, random_state=42)

model.fit(X_train_scaled)
test_labels = model.predict(X_test_scaled)

scaler = StandardScaler()

X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

tsne = TSNE(n_components=2, learning_rate=250, random_state=42)
X_test_tnse = tsne.fit_transform(X_test_scaled)


rcParams["figure.figsize"] = 10, 7
plt.scatter(X_test_tnse[:, 0], X_test_tnse[:, 1], c=test_labels)
plt.show()

print(f"Средние значения price в разных кластерах для тестового набора: "
      f"{[y_test['price'].values[test_labels == i].mean() for i in range(3)]}")
print(f"Средние значения CRIM в разных кластерах для тестового набора: "
      f"{[X_test['CRIM'].values[test_labels == i].mean() for i in range(3)]}")