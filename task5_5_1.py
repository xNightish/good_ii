import numpy as np

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
    y = np.argmin(np.abs(data_x[:, np.newaxis] - ma).sum(axis=2), axis=1)
    ma = np.array([data_x[y == m].mean(axis=0) for m in range(K)])

# Преобразование результата
X = [list(map(tuple, data_x[y == m])) for m in range(K)]

# Вывод результата
print(*X, sep='\n')

























