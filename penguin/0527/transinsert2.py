import sys
from datetime import date as dt  # 変数名を変更
from database import session
from trans_tables import Stations

def main(args):
    if len(args) < 6:
        print("引数が不足しています。正しい形式でプログラムを実行してください。")
        return

    try:
        # 引数から情報を取得
        date_str = args[1]
        departure = args[2]
        arrival = args[3]
        via = args[4]
        amount = int(args[5])

        # 日付文字列をdateオブジェクトに変換
        date = dt.fromisoformat(date_str)  # 変数名を変更

        # 新しいレコードを作成
        station = Stations(
            date=date,
            departure=departure,
            arrival=arrival,
            via=via,
            amount=amount
        )

        # 連番を付与するためのクエリ
        last_station = session.query(Stations).order_by(Stations.seq.desc()).first()
        if last_station:
            seq = last_station.seq + 1
        else:
            seq = 1

        # 連番を設定
        station.seq = seq

        # INSERT処理
        session.add(station)

        # コミット
        session.commit()

        print("交通費精算テーブルにデータを登録しました")

    except (IndexError, ValueError) as e:
        print("引数の形式が正しくありません。正しい形式でプログラムを実行してください。")
        print("エラー: ", str(e))

if __name__ == "__main__":
    main(sys.argv)
