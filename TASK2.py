a=float(input('Длина грани куба:'))/2
x1=abs(float(input('Координата точки х:')))
y1=abs(float(input('Координата точки y:')))
z1=abs(float(input('Координата точки z:')))
if x1<=a and y1<=a and z1<=a:
    print('Принадлежит')
else:
    print('Не принадлежит')    
