from my_module2 import Complex

# 2. Розробити модуль, в якому описати клас COMPLEX (комплексне число) 
# з властивостями: Real (дійсна частина), Imaginary (уявна частина). Написати для 
# цього класу методи: конструктор класу, декструктор класу, SetReal (встановлює 
# значення дійсної частини числа), SetImaginary (встановлює значення уявної 
# частини числа), ShowComplex (виводить дійсну і уявну частину на екран). В 
# основній програмі створит 2 екземпляри класу COMPLEX, виконати над цими 
# об´єктами такі дії: додавання і віднімання.  

# Створюємо 2 екземпляри класу
f = Complex(5, "3")
s = Complex(2, "6")


if f.Imaginary + s.Imaginary < 0:
    sumc = f"{f.Real + s.Real} - {abs(f.Imaginary + s.Imaginary)}i"
else:
    sumc = f"{f.Real + s.Real} + {f.Imaginary + s.Imaginary}i"


if f.Imaginary - s.Imaginary < 0:
    razc = f"{f.Real - s.Real} - {abs(f.Imaginary - s.Imaginary)}i"
else:
    razc = f"{f.Real - s.Real} + {abs(f.Imaginary - s.Imaginary)}i"


print(sumc)
print(razc)


