###素数を判定しよう###
import sys

# コマンドライン引数の取得
args = sys.argv

get_num = int(args[1])

# 引数の範囲チェック
if get_num < 1:
    print("1以上の数値を指定してください。",end="")
    
elif get_num >= 1000:
    print("1000以上は判定できません",end="")
    
else:
    # 素数判定
    is_prime = True
    if get_num > 1:
        for i in range(2, int(get_num**0.5) + 1):
            if get_num % i == 0:
                is_prime = False
                break

    # 結果を出力
    if is_prime and get_num != 2:
        print("Prime", end="")
    else:
        print("not", end="")

