from tkinter import *
import json


# 1. Написати програму-перекладач, яка буде виводити англійський 
# переклад українського слова. Сам словник повинен міститися у файлі JSON. 
# Початкові параметри вікна: ширина – 630, висота – 400, колір тла – блактитний. 
# Використати менеджер геометрії grid(). 


def translate():
    
    word = pole.get().lower().strip()

    
    with open("dict.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    
    if word in data.keys():
        L2.config(text=f"{word} - {data[word]}")
    else:
        L2.config(text=f"Невідоме слово - {word}")



win = Tk()
win.geometry("630x400")
win.configure(bg='blue')


L1 = Label(win, text="Введіть слово українською ...", bg="blue", foreground="White")
L2 = Label(win, text="", bg="blue", foreground="White")
pole = Entry(border=7)
but = Button(text="Перекласти", bg="red", foreground="white", border=5, command=translate)


L1.grid(row=0, column=1, padx=210, pady=30)
L2.grid(row=1, column=1, padx=210)
pole.grid(row=2,column=1, padx=210, pady=60)
but.grid(row=3,column=1, padx=210)


win.mainloop()