from tkinter import *

# 2. Розробити екранний додаток, який зчитає з файла речення, у якому 
# слова розділені пробілами, і виведе ці слова, відсортувавши за алфавітом, у 
# поле Text у стовпчик. Вікно програми повинно містити віджети: кнопка, фрейм, 
# поле Text. 


def doSort():
    with open("file.txt", "r", encoding="utf-8") as f:
        data = f.read().split()

    
    data.sort()
    T.delete(1.0, END)
    T.insert(1.0, "\n".join(data) )



win = Tk()
win.geometry("300x300")
win.configure(bg='blue')


with open("file.txt", "r", encoding="utf-8") as f:
    data = f.read().split()


f = Frame(win, background="red")
T = Text(f, border=5, height=10, width=20)

T.insert(1.0, "\n".join(data))
but = Button(text="Відсортувати", bg="red", foreground="white", border=5, command=doSort)


f.pack(expand=True)
T.pack()
but.pack(side="bottom")


win.mainloop()