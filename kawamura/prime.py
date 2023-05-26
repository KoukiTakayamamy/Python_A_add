import sys
args = sys.argv

number_1 = int(args[1])
number = number_1

list_1 = []

i = 2

while i != number or number_1 >= 1000:
    if number == 1:
        break
    if number % i == 0:
        number = number / i
        list_1.append(i)
    if number % i != 0:
        i = i + 1

list_1.append(i) 
if number_1 < 1000:
    if len(list_1) > 1 or number_1 == 1:
        print("not",end="")
    elif len(list_1) == 1:
        print("prime",end="")
else:
    print("1000以上は判定できません",end="")
