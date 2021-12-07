# *Задание 4
# В этом задании мы будем работать с датасетом, с которым мы уже знакомы по домашнему заданию по библиотеке Matplotlib,
# это датасет Credit Card Fraud Detection.Для этого датасета мы будем решать задачу классификации - будем определять,
# какие из транзакциции по кредитной карте являются мошенническими.Данный датасет сильно несбалансирован
# (так как случаи мошенничества относительно редки),так что применение метрики accuracy не принесет пользы и не поможет
# выбрать лучшую модель.Мы будем вычислять AUC, то есть площадь под кривой ROC.
# Импортируйте из соответствующих модулей RandomForestClassifier, GridSearchCV и train_test_split.
# Загрузите датасет creditcard.csv и создайте датафрейм df.
# С помощью метода value_counts с аргументом normalize=True убедитесь в том, что выборка несбалансирована.
# Используя метод info, проверьте, все ли столбцы содержат числовые данные и нет ли в них пропусков.Примените следующую
# настройку, чтобы можно было просматривать все столбцы датафрейма:
# pd.options.display.max_columns = 100.
# Просмотрите первые 10 строк датафрейма df.
# Создайте датафрейм X из датафрейма df, исключив столбец Class.
# Создайте объект Series под названием y из столбца Class.
# Разбейте X и y на тренировочный и тестовый наборы данных при помощи функции train_test_split, используя аргументы:
# test_size=0.3, random_state=100, stratify=y.
# У вас должны получиться объекты X_train, X_test, y_train и y_test.
# Просмотрите информацию о их форме.
# Для поиска по сетке параметров задайте такие параметры:
# parameters = [{'n_estimators': [10, 15],
# 'max_features': np.arange(3, 5),
# 'max_depth': np.arange(4, 7)}]
# Создайте модель GridSearchCV со следующими аргументами:
# estimator=RandomForestClassifier(random_state=100),
# param_grid=parameters,
# # scoring='roc_auc',
# cv=3.
# Обучите модель на тренировочном наборе данных (может занять несколько минут).
# Просмотрите параметры лучшей модели с помощью атрибута best_params_.
# Предскажите вероятности классов с помощью полученнной модели и метода predict_proba.
# Из полученного результата (массив Numpy) выберите столбец с индексом 1 (вероятность класса 1) и запишите
# в массив y_pred_proba. Из модуля sklearn.metrics импортируйте метрику roc_auc_score.
# Вычислите AUC на тестовых данных и сравните с результатом,полученным на тренировочных данных,
# используя в качестве аргументов массивы y_test и y_pred_proba.

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_auc_score


df = pd.read_csv("creditcard.csv")
print(df["Class"].value_counts(normalize=True))

pd.options.display.max_columns = 100
print(df.info())
print(df.head(10))
X = df.drop("Class", axis=1)
print(X.head(10))
y = df["Class"]
print("\n")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)
print("\nФорма X_train:")
print(X_train.shape)
print("\nФорма X_test:")
print(X_test.shape)
print("\nФорма y_train:")
print(y_train.shape)
print("\nФорма y_test:")
print(y_test.shape)

parameters = [{'n_estimators': [10, 15], 'max_features': np.arange(3, 5), 'max_depth': np.arange(4, 7)}]
#clf = GridSearchCV(
#    estimator=RandomForestClassifier(random_state=100),
#    param_grid=parameters,
#    scoring='roc_auc',
#    cv=3)
# print(clf.best_params_)

# Вычисления действительно заняли пару минут.
# были получены результаты
#clf.best_params_ = {'max_depth': 6, 'max_features': 3, 'n_estimators': 15}
clf = RandomForestClassifier(max_depth=6, max_features=3, n_estimators=15)

clf.fit(X_train, y_train)

y_pred = clf.predict_proba(X_test)
y_pred_proba = y_pred[:, 1]
print(f"roc_auc_score = {roc_auc_score(y_test, y_pred_proba)}")