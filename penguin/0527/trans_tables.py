import sys
from sqlalchemy import Column, Integer, VARCHAR, DATE
from database import Base
from database import ENGINE

# テーブル:　Stationsの定義
class Stations(Base): #大文字で定義されることが多い
    __tablename__= 'transport'
    date = Column('date', DATE(),primary_key= True) # 利用日: date
    seq = Column('seq',Integer(), primary_key= True) # 駅番号：seq/int/key=True
    departure = Column('departure', VARCHAR(20)) # 出発地: departure
    arrival = Column('arrival', VARCHAR(20)) # 到着地: arrival
    via =  Column('via', VARCHAR(40)) # 経由/利用交通機関: via
    amount = Column('amount', Integer()) # 金額: int

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__=="__main__":
    main(sys.argv)