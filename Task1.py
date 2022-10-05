s = input("Введіть рядок символів: ")
res_count = {} #словарь

s = list(s.lower())

for i in s:
    if i not in res_count.keys():
        res_count[i] = s.count(i)

print(res_count) 

#for k, v in res_count.items():
     #print(f"{k} - {v}")