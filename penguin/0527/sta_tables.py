import sys
from sqlalchemy import Column, Integer, VARCHAR, NUMERIC
from database import Base
from database import ENGINE

# テーブル:　Stationsの定義
class Stations(Base): #大文字で定義されることが多い
    __tablename__= 'station'
    seq = Column('seq',Integer(), primary_key= True) # 駅番号：seq/int/key=True
    name = Column('name',VARCHAR(20)) # 駅名 
    kilo = Column('kilo',NUMERIC(6,2)) # 東京駅からの距離 

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__=="__main__":
    main(sys.argv)