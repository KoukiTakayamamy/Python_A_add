from database import session
from trans_tables import Stations

# データの取得
records = session.query(Stations).all()

# テキストファイルへの書き込み
with open('/home/matcha-23training/python_project/Python_A_add/penguin/0527/Seminar/python/output/output.txt', mode="w", encoding="utf-8") as f:
    for record in records:
        line = f'"{record.date}", "{record.departure}", "{record.arrival}", "{record.via}", "{record.amount}"\n'
        f.write(line)

print("テキストファイルが作成されました。")
