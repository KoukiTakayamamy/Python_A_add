import sys

args = sys.argv

from decimal import Decimal, ROUND_HALF_UP

karaage_num = int(args[1])
curry_num = int(args[2])

karaage_price = karaage_num * 760
curry_price = curry_num * 850

calc_price =  karaage_price + curry_price



karaage_cost = Decimal(karaage_price * 0.323 ).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
curry_cost = Decimal(curry_price * 0.284 ).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
result_cost = karaage_cost + curry_cost

#粗利の計算
karaage_profit = karaage_price - karaage_cost
curry_profit = curry_price - curry_cost
result_profit = karaage_profit + curry_profit


print(f"売上高：{calc_price}、原価：{result_cost}、粗利：{result_profit}",end="")
