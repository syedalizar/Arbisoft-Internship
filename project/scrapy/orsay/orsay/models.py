from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float,
    Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class OrsayDB(DeclarativeBase):
    __tablename__= "product_table"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(100))
    price = Column("price", String(100))
    currency= Column("currency", String(100))
    colors = Column("colors", Text())
    sizes = Column("sizes", String(100))
    availability_status = Column("availability_status", String(100))
    category = Column("category", String(100))
