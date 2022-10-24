a = "aoeyui"
b = "qwrtpsdfghjklzxcvbnm"
nums = "1234567890"
      
amount_a = 0
amount_b = 0
amount_nums = 0

f = open("story.txt", "r")
s = f.read()
f.close()

for i in s:
    if i in a:
        amount_a += 1
    elif i in b:
        amount_b += 1
    elif i in nums:
        amount_nums += 1

print(amount_a, amount_b, amount_nums)
