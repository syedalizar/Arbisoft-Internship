# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OrsayItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    currency= scrapy.Field()
    colors = scrapy.Field()
    sizes = scrapy.Field()
    availability_status = scrapy.Field()
    category = scrapy.Field()
