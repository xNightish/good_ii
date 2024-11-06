import numpy as np
import matplotlib.pyplot as plt

# Установим случайное начальное состояние для воспроизводимости
np.random.seed(0)

# Данные
data_x = np.array([(48, 118), (74, 96), (103, 82), (135, 76), (162, 79), 
                   (184, 97), (206, 111), (231, 118), (251, 118), (275, 110), 
                   (298, 86), (320, 68), (344, 62), (376, 61), (403, 75), 
                   (424, 95), (440, 114), (254, 80), (219, 85), (288, 66), 
                   (260, 92), (201, 76), (162, 66), (127, 135), (97, 143), 
                   (83, 160), (82, 177), (88, 199), (105, 205), (135, 208), 
                   (151, 198), (157, 169), (153, 152), (117, 158), (106, 168), 
                   (106, 185), (123, 188), (125, 171), (139, 163), (139, 183), 
                   (358, 127), (328, 132), (313, 146), (300, 169), (300, 181), 
                   (308, 197), (326, 206), (339, 209), (370, 199), (380, 184), 
                   (380, 147), (343, 154), (329, 169), (332, 184), (345, 185), 
                   (363, 159), (361, 177), (344, 169), (311, 175), (351, 89), 
                   (134, 96)])

# Вычисление средних и дисперсий
M = np.mean(data_x, axis=0)      # средние по каждой координате
D = np.var(data_x, axis=0)       # дисперсии по каждой координате
K = 3                            # число кластеров

# Начальные центры кластеров
ma = np.array([np.random.normal(M, np.sqrt(D / 10), 2) for _ in range(K)])

# Алгоритм k-средних
for n in range(10):  # фиксированное количество итераций
    # Присвоение точек к ближайшему центру кластера и обновление центров кластеров
    y = np.argmin(np.sum(np.abs(data_x[:, np.newaxis] - ma), axis=2), axis=1)
    ma = np.array([data_x[y == m].mean(axis=0) for m in range(K)])

# Преобразование результата
X = [list(map(tuple, data_x[y == m])) for m in range(K)]

# Визуализация
plt.figure(figsize=(10, 8))

# Создание сетки для предсказания кластеров
x_min, x_max = data_x[:, 0].min() - 10, data_x[:, 0].max() + 10
y_min, y_max = data_x[:, 1].min() - 10, data_x[:, 1].max() + 10
xx, yy = np.meshgrid(np.arange(x_min, x_max, 1), np.arange(y_min, y_max, 1))

# Предсказание кластеров для каждой точки на сетке
Z = np.argmin(np.sum(np.abs(np.c_[xx.ravel(), yy.ravel()] - ma[:, np.newaxis]), axis=2), axis=0)
Z = Z.reshape(xx.shape)


# Отображение точек данных
for i in range(K):
    cluster_points = np.array(X[i])
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Кластер {i+1}')

# Отображение центров кластеров
plt.scatter(ma[:, 0], ma[:, 1], color='black', marker='X', s=200, label='Центры кластеров')

# Настройка графика
plt.title('Кластеризация k-средних')
plt.xlabel('Координата X')
plt.ylabel('Координата Y')
plt.legend()
plt.grid()
plt.show()
