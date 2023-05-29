from database import session    
from tables import Transport
from datetime import datetime
import sys

args = sys.argv

file_name = args[1]

list = session.query(Transport).all()

with open(f"../../../files/{file_name}.txt", mode="w", encoding="utf-8") as f:  
    for list_data in list:
        f.write("\"" + (datetime.strftime(list_data.date,"%Y%m%d")) \
                + "\",\"" + str(list_data.seq) + "\",\"" + list_data.departure + "\",\"" + list_data.arrival \
                + "\",\"" +list_data.via +"\",\"" + str(list_data.amount) +"\"\n")