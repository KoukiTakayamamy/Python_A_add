import sys
from database import session
from distance_table import Stations
from sqlalchemy import desc
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv
station1 = args[1]
station2 = args[2]

# データベースから駅名と距離を参照
station1_kilo = session.query(Stations.kilo).filter_by(name = station1).first()
station2_kilo = session.query(Stations.kilo).filter_by(name = station2).first()

# 第二引数と第三引数に設定した駅名間の距離
distance = station1_kilo[0] - station2_kilo[0]

# 少数第二位まで出力
distance = round(distance,2)
distance = abs(distance)

print(distance)

print(station1_kilo[0],station2_kilo[0])