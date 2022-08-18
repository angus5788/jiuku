# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JiukuItem(scrapy.Item):

    UserName = scrapy.Field()
    songName = scrapy.Field()
    pic = scrapy.Field()
    mp3 = scrapy.Field()
    lrc = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()

