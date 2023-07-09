import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('data.txt')
drift_time = np.zeros(4)
drift_velocity = np.zeros(4)
for i in range(4):
    y_res, x_res, _ = plt.hist(data[:, i], bins=100, alpha=1, color='white', edgecolor="black")
    left_border = 0
    right_border = 0
    for j in range(1, len(y_res)):
        if y_res[j] > 200:
            left_border = x_res[j]
            break
    for j in range(len(y_res) - 1, 0, -1):
        if y_res[j] > 200:
            right_border = x_res[j]
            break
    drift_time[i] = right_border - left_border
    drift_velocity[i] = (250 / drift_time[i]) * 1E3
    print(f"Максимальное время дрейфа t{i + 1} = {drift_time[i]} нс")
    print(f"Скорость дрейфа (t{i + 1}) = {drift_velocity[i]} мм/мкс")
    plt.xlabel(f'Время дрейфа t{i + 1}, нс', fontname='Times New Roman', size='14')
    plt.ylabel('События', fontname='Times New Roman', size='14')
    plt.show()