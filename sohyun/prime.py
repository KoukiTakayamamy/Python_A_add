# 인수로 받은 정수가 소수인지 판정
    # 소수 : 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 것
# 기수이면 'Prime'
# 소수 이외면, 'not'
# 1000 이상이면, "1000以上は判定できません"
import sys
args = sys.argv
num = int(args[1])

# num < 1000 이라면 소수인지 아닌지 판별하기
# 소수인지 판정하는 함수
def is_prime(num):
    # num >= 1000 이라면 판정 불가
    if num >= 1000:
        return "1000以上は判定できません"
    # 1은 소수가 아님
    if num == 1:
        return "not" # 소수 아님
    # 2~(num-1)까지의 수로 나누어보기
    for i in range(2, num):
        if num % i == 0:
            return "not" # 소수 아님
        else:
            return "Prime" # 소수
    
result = is_prime(num)
print(result, end="")