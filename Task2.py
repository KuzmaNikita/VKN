import json

# 2. Текстовий файл містить дані про назви і довжини сторін трикутника у 
# форматі JSON. Написати програму, яка: 1) перевірить існування трикутника; 2) 
# виведе вид трикутника (прямокутний, рівнобедрений, рівносторонній). 

f = open("data.json", "r")

data = json.load(f)
keys = list(data.keys())
f.close()

if data[keys[0]] < data[keys[1]] + data[keys[2]]:
    print("Трикутник існує")
    if data[keys[0]] == data[keys[1]] and data[keys[0]] == data[keys[2]]:
        print("Рівносторонній") 
    else:

        if data[keys[0]] ** 2 == (data[keys[1]] ** 2 + data[keys[2]] ** 2) or data[keys[1]] ** 2 == (data[keys[0]] ** 2 + data[keys[2]] ** 2) or data[keys[2]] ** 2 == (data[keys[1]] ** 2 + data[keys[0]] ** 2):
            
            if data[keys[0]] == data[keys[1]] or data[keys[0]] == data[keys[2]] or data[keys[2]] == data[keys[1]]:
                print("Прямокутний рівнобедренний")
            else:
                print("Прямокутний")


        else:
            if data[keys[0]] == data[keys[1]] or data[keys[0]] == data[keys[2]] or data[keys[2]] == data[keys[1]]:
                print("Рівнобедренний")

else:
    print("Трикутник не існує")