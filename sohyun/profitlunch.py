# 가라아게 정식 : 760엔, 원가율 32.3%
# 카레 세트 : 850엔, 원가율 28.4%
# 각각의 1일의 주문 수를 인수에 설정하면,
# 1일의 매상고, 원가, 粗利를 계산

# 매상 총이익 : 매상고에서 매상 원가를 뺀 이익
# 원가율 : 제품의 최종 가격에서 원가가 차지하는 비율

# 소수 제1에서 반올림 해, 정수치로 원가를 산출
from decimal import Decimal, ROUND_HALF_UP
import sys

args = sys.argv
# 개수
kara_count = int(args[1])
curry_count = int(args[2])
# 가격
kara_cost = 760
curry_cost = 850 
# 각 원가
kara_price_cost = kara_count * kara_cost * 0.323
curry_price_cost = curry_count * curry_cost * 0.284

kara_price_cost = Decimal(str(kara_price_cost)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
curry_price_cost = Decimal(str(curry_price_cost)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

sum_cost = (kara_count * kara_cost) + (curry_count * curry_cost) # 매상고
sum_price_cost = kara_price_cost + curry_price_cost # 총 원가 가격

gross_profit = sum_cost - sum_price_cost # 매상 총이익

print("売上高：" + str(sum_cost) + "、原価：" + str(sum_price_cost) + "、粗利：" + str(gross_profit), end="")