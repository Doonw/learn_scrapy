# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HelloItem(scrapy.Item):
    title = scrapy.Field(serializer=lambda x:x[0])
    date = scrapy.Field(serializer=str)
    image_urls = scrapy.Field(serializer=str)
    tags = scrapy.Field(serializer=str)
    image_paths = scrapy.Field()

class ImageSet(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    image_path = scrapy.Field()