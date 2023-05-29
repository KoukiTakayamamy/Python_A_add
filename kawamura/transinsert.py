from datetime import date
from database import session
from station_table import Transport
import sys

args = sys.argv

registration_date = int(args[1])
sequence = int(args[2])
place_1 = args[3]
place_2 = args[4]
Train_line = args[5]
fare = int(args[6])

year = registration_date % 10000
month = year % 100

duplicate_date = session.query(Transport).filter_by(date = date((registration_date // 10000), year // 100, month % 100),seq = number).count() 

print(duplicate_date)

transport= Transport(
        date = date((registration_date // 10000), year // 100, month % 100),
        seq = sequence,
        departure = place_1,
        arrival = place_2,
        via = Train_line,
        amount = fare
    )

if duplicate_date != 1:
    # 指定した日を追記
    transport= Transport(
        date = date((registration_date // 10000), year // 100, month % 100),
        seq = sequence,
        departure = place_1,
        arrival = place_2,
        via = Train_line,
        amount = fare
    )
    print("交通費精算テーブルにデータを登録しました")
else:
    print("error:交通費精算テーブルにデータを登録できませんでした")
    exit(0)

session.add(transport)

session.commit()
