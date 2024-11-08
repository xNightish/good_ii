from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter

def minkowski_distance(x_k, x_m, p, weights=None):
    if weights is None:
        weights = np.ones_like(x_k)  # Если веса не заданы, используем единичные веса
    return (np.sum(weights * np.abs(x_k - x_m) ** p)) ** (1/p)

def knn_predict(x_train, y_train, x_test, k, p):
    predictions = []
    for test_point in x_test:
        # Вычисляем расстояния до всех обучающих образцов
        distances = [minkowski_distance(test_point, train_point, p) for train_point in x_train]
        
        # Получаем индексы k ближайших соседей
        k_indices = np.argsort(distances)[:k]
        
        # Получаем классы ближайших соседей
        k_nearest_labels = [y_train[i] for i in k_indices]
        
        # Голосуем за класс
        most_common = Counter(k_nearest_labels).most_common(1)
        predictions.append(most_common[0][0])
    
    return np.array(predictions)

data_x = [(4.9, 3.3), (5.6, 4.5), (6.4, 4.3), (6.7, 5.7), (6.3, 5.0), (5.2, 3.9), (5.5, 3.7), (5.6, 3.6), (5.5, 3.8), (6.1, 4.7), (7.4, 6.1), (6.0, 5.1), (5.5, 4.4), (5.9, 5.1), (6.5, 5.8), (6.5, 4.6), (6.7, 4.4), (6.3, 5.6), (5.9, 4.8), (6.0, 4.5), (5.6, 4.1), (5.6, 4.9), (4.9, 4.5), (6.2, 4.5), (6.1, 4.7), (6.1, 4.9), (6.2, 5.4), (5.7, 4.2), (6.1, 5.6), (5.8, 4.0), (6.6, 4.6), (5.6, 4.2), (7.2, 6.1), (7.7, 6.7), (5.6, 3.9), (7.7, 6.9), (6.0, 4.0), (6.1, 4.0), (7.6, 6.6), (5.1, 3.0), (6.3, 6.0), (6.7, 5.7), (6.8, 5.9), (6.4, 5.5), (7.0, 4.7), (5.8, 5.1), (5.8, 5.1), (6.4, 5.3), (6.3, 4.9), (6.4, 5.3), (5.7, 3.5), (7.2, 5.8), (6.4, 5.6), (5.7, 4.5), (6.0, 4.5), (7.7, 6.1), (6.2, 4.3), (7.1, 5.9), (7.3, 6.3), (5.0, 3.3), (6.3, 5.1), (5.8, 3.9), (6.4, 4.5), (6.3, 5.6), (6.8, 5.5), (6.9, 5.4), (5.5, 4.0), (5.7, 4.1), (6.5, 5.5), (6.3, 4.7), (5.0, 3.5), (6.7, 5.8), (6.9, 4.9), (7.7, 6.7), (5.8, 4.1), (6.4, 5.6), (6.7, 5.2), (6.7, 4.7), (5.4, 4.5), (6.8, 4.8), (5.7, 4.2), (5.5, 4.0), (6.3, 4.9), (6.5, 5.2), (5.8, 5.1), (6.0, 4.8), (6.2, 4.8), (6.5, 5.1), (7.9, 6.4), (6.7, 5.0), (6.7, 5.6), (6.0, 5.0), (6.1, 4.6), (5.7, 5.0), (7.2, 6.0), (6.3, 4.4), (5.9, 4.2), (6.9, 5.1), (6.6, 4.4), (6.9, 5.7)]
data_y = [-1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1]

data_x = np.array(data_x)
data_y = np.array(data_y)

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, random_state=123,test_size=0.3, shuffle=True)

k = 5
p=1

# Прогнозируем классы для тестовой выборки
predict = knn_predict(x_train, y_train, x_test, k, p)

# Вычисляем количество неправильных предсказаний
Q = sum(predict != y_test)

# Выводим результаты
print("Прогнозы для тестовой выборки:", predict)
print("Количество неправильных предсказаний:", Q)

import matplotlib.pyplot as plt

# Визуализация тестовых данных
plt.figure(figsize=(10, 6))

# Отображаем тестовую выборку
plt.scatter(x_test[y_test == -1][:, 0], x_test[y_test == -1][:, 1], color='red', label='Класс -1 (Тестовая выборка)', marker='o')
plt.scatter(x_test[y_test == 1][:, 0], x_test[y_test == 1][:, 1], color='blue', label='Класс 1 (Тестовая выборка)', marker='o')

# Отображаем неправильные классификации
wrong_predictions = x_test[predict != y_test]
plt.scatter(wrong_predictions[:, 0], wrong_predictions[:, 1], color='black', label='Неправильная классификация', marker='x', s=100)

# Настройки графика
plt.title('Классификация с использованием метода ближайших соседей', fontsize=16)
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.legend()
plt.grid()
# plt.savefig('task5_1_1.png')
plt.show()





