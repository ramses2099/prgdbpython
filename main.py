import sys, os
import psycopg2
from pathlib import Path
from sqlalchemy import URL, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.types import Integer, String
 
class Base(DeclarativeBase):
    pass

class Cars(Base):
    __tablename__ = "cars"


def connection_postgres() -> None:
    """
    Function connection postgres with psycop2 driver
    """
    try:
        conn = psycopg2.connect("host=localhost dbname=test user=postgres password=S3cret")
        cur = conn.cursor()
        sql = Path(os.path.join(os.path.dirname(__file__),"query_count_brand_state.sql")).read_text()
        cur.execute(sql)
        res = cur.fetchall()
        print(res)

        cur.close()
        conn.close()   
    
    except Exception as ex:
        print(ex)



def main() -> None:
   os.system("clear")
   print("ok")

if __name__ == "__main__":
    main()