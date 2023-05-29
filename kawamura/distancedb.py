import sys
import sys
from database import session
from station_table import Stations

args = sys.argv

place_1 = args[1] 
place_2 = args[2]

place_distance_1 = session.query(Stations.kilo).filter_by(name = place_1).first() # 一つ目の場所の東京からの距離
place_distance_2 = session.query(Stations.kilo).filter_by(name = place_2).first() # 二つ目の場所の東京からの距離


distance_between = place_distance_1[0] - place_distance_2[0] # 距離を求める

print(abs(round(distance_between,2)), end="") # 四捨五入小数点第二位までかつ絶対値を指定