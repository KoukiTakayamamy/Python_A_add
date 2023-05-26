import sys
args = sys.argv
num = int(args[1])

# 上限を設定
limit = 1000

# 入力値が上限を超える場合の出力
if num >= limit:
    print(f"{limit}以上は判定できません", end ="")

else:
    for i in range(2, num):
        if num % i == 0:
            n = 1
            break
        else:
            n = 0
    if n == 1:
        print("not", end ="")
    
    else:
        print("Prime", end ="")


'''
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
'''
