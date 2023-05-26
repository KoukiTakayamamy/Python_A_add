# 택시의 운임이 처음 1500m까지는 630엔,
# 이후는 344m마다 98엔
# 인수로 승차거리(m)를 건네, 운임을 계산해라

# import math
import sys
args = sys.argv
distance = int(args[1])

# 거리가 1500 이하일 때
if distance <= 1500:
    cost = 630
# 거리가 1500 초과일 때
else:
    leftDistance = distance - 1500
    addCost = (leftDistance // 344) * 98 # // : 切り捨て
    # addCost = round(leftDistance / 344) * 98 # round의 경우, 0.5 -> 1이 됨
    
    # 남은 거리가 344로 나누어 떨어지면
    if leftDistance % 344 == 0:
        cost = 630 + addCost
    # 344로 안 나누어 떨어지면
    else:
        cost = 630 + addCost + 98

print(str(cost), end="")