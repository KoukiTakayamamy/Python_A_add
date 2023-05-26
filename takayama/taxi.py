import sys

args = sys.argv

input_num = int(args[1])

price = 630

if(input_num > 1500):
    add_dis = input_num - 1500
    add_cnt = add_dis // 344

    price = price + ((add_cnt+1)  * 98)

    
print(price,end="")
