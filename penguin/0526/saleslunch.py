###ランチの売り上げを計算しよう###
import sys 

args= sys.argv
lunch_chicken = int(args[1])
lunch_curry= int(args[2])

chicken_sales= 760 * lunch_chicken
curry_sales= 850 * lunch_curry
daily_sales= chicken_sales + curry_sales

print(daily_sales,end="")