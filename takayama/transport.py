from datetime import datetime
from database import session
from tables import Transport
import sys

#引数
args = sys.argv

try:    
    insdata = Transport(
        date = datetime.strptime(args[1], "%Y%m%d"),#文字列をデータ型に変換
        seq = int(args[2]),
        departure = args[3],
        arrival = args[4],
        via = args[5],
        amount = int(args[6])
    )

    #INSERT
    session.add(insdata)

    session.commit()
    print("交通費精算テーブルにデータを登録しました", end="")

except:
    session.rollback()
    print("error:交通費精算テーブルにデータを登録できませんでした", end="")
