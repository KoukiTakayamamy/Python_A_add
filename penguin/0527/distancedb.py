###新幹線の駅間を計算しよう3###
import sys
from database import session # データベースに接続
from sta_tables import Stations # テーブル定義

# コマンドライン引数の取得
args = sys.argv
get_station_name_1 = args[1] # 東京
get_station_name_2 = args[2] # 新大阪

# 駅名をキロポストに変換する
station_1 = session.query(Stations.kilo).filter(Stations.name == get_station_name_1).first()
station_2 = session.query(Stations.kilo).filter(Stations.name == get_station_name_2).first()

if station_1 is not None and station_2 is not None:
    # 絶対値で出すabs()
    sta_distance = abs(station_2.kilo - station_1.kilo)
else:
    sta_distance = None

print(sta_distance)
