import sys

karaage_order_number = int(sys.argv[1])
curry_order_number = int(sys.argv[2])

sales = karaage_order_number * 760 + curry_order_number * 850

print(str(sales),end="")