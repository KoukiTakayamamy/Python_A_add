import sys
args = sys.argv
distance = int(args[1])

# 初乗り1500mを代入
starting_distance = 1500

# 初乗り料金を代入
starting_fee = 630

# 344を代入
fixed_distance = 344

# 98円を代入
fixed_fee = 98

# 乗車距離が1500mより短い場合、料金は630円
if distance <= starting_distance:
    fee = starting_fee
# 1500m以上の場合、料金は630円に
else:
    fee = starting_fee + ((distance - starting_distance)//fixed_distance + 1) * 98

print(fee, end = "")
