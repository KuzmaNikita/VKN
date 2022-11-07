# 2. Написати програму, яка буде шифрувати і розшифровувати 
# повідомлення, міняючи місцями символи з парними і непарними індексами. 
# Для цього створити відповідну функцію. 

def crypt(s):
    s = list(s)

    # Превратили строку в список если четное количество символов то остановимся на предпоследнем иначе остановимся на предпредпоследнем
    if len(s) % 2 == 0:
        end = len(s)
    else:
        end = len(s) - 1

    # Пройдемся по списку и будем менять соседние символы местами
    for i in range(0, end, 2):
        new = s[i + 1]
        s[i + 1] = s[i]
        s[i] = new
        
    # Печатаем список превращая в строку
    return "".join(s)

def decrypt(s):
    s = list(s)

    
    if len(s) % 2 == 0:
        end = len(s)
    else:
        end = len(s) - 1

    
    for i in range(0, end, 2):
        new = s[i + 1]
        s[i + 1] = s[i]
        s[i] = new
        
    
    return "".join(s)
