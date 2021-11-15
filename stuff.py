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


def plot_date(title, x, y, x_label, y_label, plot_code='-xr', centroid='n'):
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
    plt.axis([x_min, x_max, y_min, y_max])
    plt.show()


# 2 scatter plot
t_p_values = open_file('temp_and_pressure.txt')
t_p_x, t_p_y = split_values2(t_p_values)
plot_date('Temp to Pressure', t_p_x, t_p_y, 'Temp', 'Pressure', plot_code='or', centroid='y')
