# 카라아게 정식 : 760
# 카레 세트 : 850
# 각각의 1일의 주문수를 인수로 설정 -> 1일의 매상고를 계산하는 프로그램

import sys
args = sys.argv

kara_count = int(args[1])
curry_count = int(args[2])

kara_cost = 760
curry_cost = 850

sum_cost = (kara_count * kara_cost) + (curry_count * curry_cost)

print(str(sum_cost), end="")