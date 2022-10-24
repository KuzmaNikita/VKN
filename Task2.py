import os

#disc = os.getcwd()[:3]

# Проверит только текущую папку
disc = os.getcwd()

for i in os.walk(disc):
    if "input.txt" in i[-1]:
        print(f"Файл input.txt найден по пути - {i[0]}")