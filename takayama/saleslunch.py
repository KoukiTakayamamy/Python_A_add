import sys

args = sys.argv

karaage_num = int(args[1])
curry_num = int(args[2])

calc_price = karaage_num * 760 + curry_num * 850

print(calc_price,end="")