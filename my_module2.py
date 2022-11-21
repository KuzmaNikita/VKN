# 2. Розробити модуль, в якому описати клас COMPLEX (комплексне число) 
# з властивостями: Real (дійсна частина), Imaginary (уявна частина). Написати для 
# цього класу методи: конструктор класу, декструктор класу, SetReal (встановлює 
# значення дійсної частини числа), SetImaginary (встановлює значення уявної 
# частини числа), ShowComplex (виводить дійсну і уявну частину на екран). В 
# основній програмі створит 2 екземпляри класу COMPLEX, виконати над цими 
# об´єктами такі дії: додавання і віднімання. 

class Complex():
    
    def __init__(self, Real, Imaginary):
        self.Real = int(Real)
        self.Imaginary = int(Imaginary)

    
    def __del__(self):
        print("Ми видалили число - " + str(self.Real) + " + " + str(self.Imaginary) + "i")

    
    def SetReal(self, new_real):
        self.Real = float(new_real)

    
    def SetImaginary(self, new_imaginary):
        self.Imaginary = str(new_imaginary)

    
    def ShowComplex(self):
        print(f"{self.Real} + {self.Imaginary}i")

    