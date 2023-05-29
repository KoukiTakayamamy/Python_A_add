from database import session
from tables import Stations
import sys
args = sys.argv


in_from = args[1] 
in_to = args[2]

stations = session.query(Stations).filter(Stations.name.in_([in_from, in_to])).first()

distance = abs(stations[0].kilo - stations[1].kilo)

print(f"{distance:.2f}", end="")
