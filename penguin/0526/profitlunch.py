###ランチの粗利を計算しよう###
import sys

args = sys.argv

# 引数の数をチェック
if len(args) != 3:
    print("引数には2つの数字を指定してください。")
    sys.exit(1)

# 数字を取得
try:
    lunch_chicken = int(args[1])  # 唐揚げ定食の注文数
    lunch_curry = int(args[2])  # カレーセットの注文数
except ValueError:
    print("引数には数字を指定してください。")
    sys.exit(1)

# メニューごとの情報
lunch_chicken_price = 760  # 唐揚げ定食の値段
chicken_cost_rate = 0.323  # 唐揚げ定食の原価率
lunch_curry_price = 850  # カレーセットの値段
curry_cost_rate = 0.284  # カレーセットの原価率

# 売上高の計算
chicken_sales = lunch_chicken * lunch_chicken_price  # 唐揚げ定食の売上高
curry_sales = lunch_curry * lunch_curry_price  # カレーセットの売上高
total_sales = chicken_sales + curry_sales  # 1日の合計売上高


# 原価の計算
chicken_cost = round(chicken_sales * chicken_cost_rate)  # 唐揚げ定食の原価
curry_cost = round(curry_sales * curry_cost_rate)  # カレーセットの原価
total_cost = chicken_cost + curry_cost  # 1日の合計原価

# 粗利の計算
gross_profit = total_sales - total_cost  # 1日の粗利

# 結果を出力
print(f"売上高：{total_sales}、原価：{total_cost}、粗利：{gross_profit}", end="")
