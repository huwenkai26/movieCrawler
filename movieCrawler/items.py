# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影详情的url
    moviedetailUrl = scrapy.Field()
    # 电影具体名字
    moviedetailName = scrapy.Field()
    # 电影的图片
    moviedetailImg = scrapy.Field()
    # 电影的下载链接
    movieDownUrl = scrapy.Field()


