import sys
args = sys.argv
karaage_amount = int(args[1])
curry_amount = int(args[2])

# 唐揚げ定食の価格を代入
karaage_price = 760

# カレーの価格を代入
curry_price = 850

sum = karaage_amount * karaage_price + curry_amount * curry_price

print(sum, end ="")