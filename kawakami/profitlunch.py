import sys
args = sys.argv
karaage_amount = int(args[1])
curry_amount = int(args[2])
from decimal import Decimal, ROUND_HALF_UP

# 唐揚げ定食の価格を代入
karaage_price = 760

# カレーの価格を代入
curry_price = 850

# 唐揚げ定食の原価率を代入
karaage_costrate = 32.3 * 0.01

# カレーの原価率を代入
curry_costrate = 28.4 * 0.01


# 唐揚げ定食の売上高を計算する
karaage_salse = karaage_amount * karaage_price

# 唐揚げ定食の原価を計算する
karaage_cost = karaage_salse * karaage_costrate
karaage_cost = Decimal(str(karaage_cost)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

# 唐揚げ定食の粗利を計算する
karaage_profit = karaage_salse - karaage_cost


# カレーセットの売上高を計算する
curry_salse = curry_amount * curry_price

# カレーセットの原価を計算する
curry_cost =curry_salse * curry_costrate
curry_cost = Decimal(str(curry_cost)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

# カレーセットの粗利を計算する
curry_profit = curry_salse - curry_cost


# 1日の売上高、原価、粗利を計算する
salse = karaage_salse + curry_salse
cost = karaage_cost + curry_cost
profit = karaage_profit + curry_profit

print(f"売上高：{salse}、原価：{cost}、粗利：{profit}", end = "")
