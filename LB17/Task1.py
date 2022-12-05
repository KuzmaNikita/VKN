import pandas as pd

# 1. Файл trains.csv містить номери потягів і назви маршрутів. Користувач 
# задає маршрут. Програма повинна записати у файл search.csv номери всіх 
# потягів, які рухаються за цим маршрутом (або повідомлення про їх відсутність). 
# Використати об´єкт DataFrame. 


marsh = int(input("Введіть маршрут: "))

with open("trains.csv", "r") as f:
    data = pd.read_csv(f, sep=";", encoding="utf-8")

    
    heads = data.columns.to_list()
    neded_trains = []

    for i in heads:
        train = data[i].to_list()
        if marsh in train:
            neded_trains.append(i)

    
    if len(neded_trains) == 0:
        neded_trains.append("По маршруту не знайдено потягів!")
    
    new_data = pd.DataFrame(neded_trains, columns=[marsh])

new_data.to_csv("search.csv", index=False)