from datetime import date
from database import session
from trans_tables import Stations

# 登録するデータの編集
# 利用日(date)、出発地(departure)、到着地(arrival)、経由/利用交通機関(via)、金額(amount)
station = Stations(
    date=date(2023, 6, 1),
    departure="東京",
    arrival="新宿",
    via="中央線",
    amount=200
)

# 連番を付与するためのクエリ
# 降順で並び変えておしりにある値を取ってきて、そこから+1をする処理
last_aquaattend = session.query(Stations).order_by(Stations.seq.desc()).first() 
if last_aquaattend: # もしlast_aquaend(最後の値)が存在する場合
    seq = last_aquaattend.seq + 1 # last_aquaendに+1する
else:
    seq = 1 #ない場合は1になる

# 連番を設定
station.seq = seq

# INSERT処理
session.add(station)

# コミット
session.commit()