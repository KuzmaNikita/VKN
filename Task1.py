import csv

# 1. Написати програму, яка зчитає з файла CSV кількість опадів за кожен 
# день місяця, обчислить сумарну кількість опадів, виведе на екран числа, по 
# яких кількість опадів була вищою за середньомісячну. 

f = open("data.csv", "r")

data = list(csv.reader(f))
f.close()

sum = 0
ser = 0
m_ser = []

for i in range(len(data[0])):
    sum += float(data[1][i])

ser = round(sum / len(data[1]), 3)

for i in range(len(data[0])):
    if float(data[1][i]) < ser:
        m_ser.append(data[0][i])
    
print(f"Сума опадів протягом місяця - {sum}, середня кількість опадів - {ser}")
print(f"Числа в яких було більше опадів ніж в середньому за місяць - {', '.join(m_ser)}")




