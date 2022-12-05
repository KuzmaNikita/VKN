import pylab

# 2. Текстовий файл містить масив цілих чисел, записаних у рядок. Програма 
# повинна вивести гістограму частот, з якою зустрічаються ці числа у масиві.

with open("text.txt", "r") as f:
    x = list(f.read().split())


y = [x.count(i) for i in x]


pylab.bar(x, y) 
pylab.show()
