path = input("Введите путь к файлу: ")
#path = "C:\Users\Nikita\Desktop\LB7\Task2.py"
path = path.split('\\')

for i in path[:-1]:
    print(i)

print(f"Назва файлу - {path[-1].split('.')[0]}, розширення файлу - .{path[-1].split('.')[1]}") 