from datetime import date

from database import session
from trans_tables import Transport

import sys

args = sys.argv

input_date = args[1]  # 利用日
input_seq = int(args[2])  # 連番
input_departure = args[3]  # 出発地
input_arrival = args[4]  # 到着地
input_via = args[5]  # 経由/利用交通機関
input_amount = int(args[6])  # 金額

# 日付の変換
dt = date(int(input_date[:4]), int(input_date[4:6]), int(input_date[6:]))

# dateとseqが一致するデータが既に存在するか確認
existing_transport = session.query(Transport).filter_by(date=dt, seq=input_seq).first()

if existing_transport:
    print("エラー: 交通費精算テーブルにデータを登録できませんでした。")
else:
    # 登録するデータの編集
    transport = Transport(
        date=dt,
        seq=input_seq,
        departure=input_departure,
        arrival=input_arrival,
        via=input_via,
        amount=input_amount
    )

    # INSERT処理
    session.add(transport)

    # コミット
    session.commit()

    print("交通費精算テーブルにデータを登録しました。")
