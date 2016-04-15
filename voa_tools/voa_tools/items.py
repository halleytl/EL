# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class VoaToolsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class VoaVideoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 单词
    word = Field()

    # 视频类型
    video_type = Field()

    # 视频格式
    video_css_class = Field()

    # 视频地址
    video_src = Field()

    video_desc = Field()
