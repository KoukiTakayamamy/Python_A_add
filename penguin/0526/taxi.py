###タクシー運賃を計算しよう###
import sys 

args= sys.argv
get_distance = int(args[1])

# 運賃の計算
if get_distance <= 1500:
    fare = 630
else:
    extra_distance = get_distance - 1500
    extra_blocks = (extra_distance + 343) // 344  # 追加料金のブロック数を計算
    extra_fare = extra_blocks * 98  # 追加料金を計算
    fare = 630 + extra_fare

# 結果を出力
print(fare,end="")