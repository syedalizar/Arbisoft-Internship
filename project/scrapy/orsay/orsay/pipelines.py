# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from orsay.models import OrsayDB, db_connect, create_table



# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OrsayPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

        session = self.Session()
        orsay_db=OrsayDB()

        orsay_db.name = item["name"]
        orsay_db.price = item["price"]
        orsay_db.currency = item["currency"]
        orsay_db.colors = item["colors"]
        orsay_db.sizes = item["sizes"]
        orsay_db.availability_status = item["availability_status"]
        orsay_db.category = item["category"]

        try:
            session.add(orsay_db)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
