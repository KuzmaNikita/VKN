# 3. Створити словник, який міститиме дані про ціну 7 автомобілів. 
# Програма повинна: 1) перевіряти наявність заданого автомобіля у словнику; 2) 
# дописувати до словника кілька ключів і значень; 3) виводити ціну автомобіля за 
# його назвою. 

autos = {"BMW 550 2018": 58000, "BMW 328 Xdrive 2014": 16900, "BMW X5 2015": 28400, 
        "BMW X5 2020": 82000, "Mercedes-Benz GLE 350 E AMG 2022": 85000, "Mercedes-Benz GLE 350 E 2022": 91500, 
        "Mercedes-Benz E 220 2012": 12700}

autos["Mercedes-Benz S 500 long 2021"] = 155000
autos["Ford Focus Titanium 2011"] = 8100
autos["Ford Focus TITANIUM EDITION 2014"] = 8950
print(autos)
while True:
    auto_name = input("Введіть назву автомобіля: ")

    if auto_name == "":
        break
    else:
        if auto_name in autos.keys():
            print(f"Автомобіль {auto_name} є в наявності, його вартість - {autos[auto_name]} $")

