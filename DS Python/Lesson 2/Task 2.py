#Задание 2
#С помощью функции linspace из библиотеки Numpy создайте массив t из 51 числа от 0 до 10 включительно.
#Создайте массив Numpy под названием f, содержащий косинусы элементов массива t.
#Постройте линейную диаграмму, используя массив t для координат по горизонтали,а массив f - для координат по вертикали.
#Линия графика должна быть зеленого цвета.
#Выведите название диаграммы - 'График f(t)'. Также добавьте названия для горизонтальной оси - 'Значения t' и
#для вертикальной - 'Значения f'.
#Ограничьте график по оси x значениями 0.5 и 9.5, а по оси y - значениями -2.5 и 2.5.


import numpy as np
from matplotlib import pyplot as plt
import math

#%matplotlib inline
#%config InlineBackend.figure_format = 'svg'

t = np.linspace(0, 10, 51)
f = np.cos(t)
plt.plot(t, f, color="green")
plt.title("График f(t)")
plt.xlabel("Значения t")
plt.ylabel("Значения f")
plt.axis([0.5, 9.5, -2.5, 2.5])
plt.grid(axis="x", color="lightgrey")
plt.show()
