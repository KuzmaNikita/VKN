from my_module2 import *

# 2. Написати програму, яка буде шифрувати і розшифровувати 
# повідомлення, міняючи місцями символи з парними і непарними індексами. 
# Для цього створити відповідну функцію. 


s = "Парні та непарні індекси!"
crypted_s = crypt(s)
decrypted_s = decrypt(crypted_s)

print(crypted_s)
print(decrypted_s)