from database import session
from station_table import Transport

transport_table = session.query(Transport.date,Transport.seq,Transport.departure,Transport.arrival,Transport.via,Transport.amount).all()
for line in transport_table:
    print(line)
    print(line[0])

i=0
with open("files/output.txt",mode="w",encoding="utf-8") as f:
    for line in transport_table:
        for i in range(0,6):
            if(i ==5):
                f.write("\"{0}\"".format(str(line[i])))
                continue
            f.write("\"{0}\",".format(str(line[i])))
        f.write("\n")
