import math
import matplotlib.pyplot as plt


def open_file(file_name):
    new_list1 = []
    new_list2 = []
    with open(file_name) as file:
        lines = file.readlines()
        for item in lines[1:]:
            new_list1.append(item.strip())
    for item in new_list1:
        new_list2.append(item.split('\t'))
    return new_list2


def split_values2(values):
    xs = []
    ys = []
    for item in values:
        xs.append(float(item[0]))
        ys.append(float(item[1]))
    return xs, ys


def split_values4(values):
    set1 = []
    set2 = []
    set3 = []
    set4 = []
    for item in values:
        set1.append(float(item[0]))
        set2.append(float(item[1]))
        set3.append(float(item[2]))
        set4.append(float(item[3]))
    return set1, set2, set3, set4


def find_centroid(x, y):
    counter_x = 0
    counter_y = 0
    for numb in x:
        counter_x += numb
    for numb in y:
        counter_y += numb
    x_centroid = counter_x / len(x)
    y_centroid = counter_y / len(y)
    return x_centroid, y_centroid


def plot_data(title, x, y, x_label, y_label, plot_code='-xr', centroid='n', horizontal='n', vertical='n'):
    x_min = min(x)
    x_max = max(x)
    y_max = max(y)
    y_min = min(y)
    x_centroid, y_centroid = find_centroid(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, plot_code)
    if centroid == 'y':
        plt.plot(x_centroid, y_centroid, 'xb')
        plt.text(x_centroid, y_centroid, 'This is the centroid')
        if vertical == 'y':
            plt.axvline(x=x_centroid)
        if horizontal == 'y':
            plt.axhline(y=y_centroid)
    plt.axis([x_min, x_max, y_min, y_max])


# # 1 time series plot
t_t_values = open_file('time_and_temp.txt')
t_t_x, t_t_y = split_values2(t_t_values)
plot_data('Time(s) to Temp(C)', t_t_x, t_t_y, 'Time', 'Temp', plot_code='--og')
plt.show()
# # 2 scatter plot
t_p_values = open_file('temp_and_pressure.txt')
t_p_x, t_p_y = split_values2(t_p_values)
plot_data('Temp to Pressure', t_p_x, t_p_y, 'Temp', 'Pressure', plot_code='or', centroid='y', horizontal='y', vertical='y')
plt.show()
# 3
t_t_p = open_file('time_temp_pressure_volume.txt')
time_s, temp_s, pressure_s, volume_s = split_values4(t_t_p)
plt.subplot(3, 1, 1)
plot_data('Temp to Time', temp_s, time_s, 'Temp', 'Time', plot_code='xg', centroid='y', horizontal='y')
plt.subplot(3, 1, 2)
plot_data('Pressure to Time', pressure_s, time_s, 'Pressure', 'Time', plot_code='xg', centroid='y', horizontal='y')
plt.subplot(3, 1, 3)
plot_data('Volume to Time', volume_s, time_s, 'Volume', 'Time', plot_code='xg', centroid='y', horizontal='y')
plt.show()
