import pandas as pd


# 2. Файл tetraedr.json містить імена і координати у просторі вершин 
# тетраедра (подані у вигляді словника). Написати програму, яка: 1) зчитає дані у 
# масив Series; 2) обчислить об´єм тетраедра; 3) збереже результат у файл 
# volume.json. 


data = pd.read_json("tetraedr.json")


heads = data.columns.to_list()
coords = []
s_data = []
s_indexes = []

for i in heads:
    coords.append(data[i].to_list())
    s_data.extend(data[i].to_list())
    s_indexes.extend([f"{i}x", f"{i}y", f"{i}z"])



V1_tetr = []


V1_tetr.append([coords[1][0] - coords[0][0], coords[1][1] - coords[0][1], coords[1][2] - coords[0][2]])
V1_tetr.append([coords[2][0] - coords[0][0], coords[2][1] - coords[0][1], coords[2][2] - coords[0][2]])
V1_tetr.append([coords[3][0] - coords[0][0], coords[3][1] - coords[0][1], coords[3][2] - coords[0][2]])


V_tetr = 1/6 * abs((V1_tetr[0][0] * V1_tetr[1][1] * V1_tetr[2][2]) + (V1_tetr[0][1] * V1_tetr[1][2] * V1_tetr[2][0])+ (V1_tetr[0][2] * V1_tetr[1][0] * V1_tetr[2][1]) - (V1_tetr[0][2] * V1_tetr[1][1] * V1_tetr[2][0]) - (V1_tetr[0][0] * V1_tetr[1][2] * V1_tetr[2][1]) - (V1_tetr[0][1] * V1_tetr[1][0] * V1_tetr[2][2]))

s_data.append(V_tetr)
series_data = pd.Series(s_data, index=s_indexes + ["V tetraedra"])

series_data.to_json("volume.json")