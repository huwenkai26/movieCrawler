# -*- coding: utf-8 -*-
from lxml import etree
import scrapy
from movieCrawler.items import MoviecrawlerItem

class Dytt8Spider(scrapy.Spider):
    name = 'dytt8'
    baseURl = 'http://www.dytt8.net'
    allowed_domains = ['www.dytt8.net/']
    start_urls = ['http://www.dytt8.net']

    def parse(self, response):
        for deatilUrl in response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/ul/tr/a/@href'):
            # print(deatilUrl.extract())
            yield scrapy.Request(self.baseURl+deatilUrl.extract(),callback=self.secondParse,dont_filter=True)
    def secondParse(self,response):
        item =MoviecrawlerItem()

        item['moviedetailName']= response.xpath('//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/h1/font/text()')[0].extract()

        item['movieDownUrl']    = response.xpath(r'//*[@id="Zoom"]/descendant::a/text()')[0].extract()

        item['moviedetailImg']  = response.xpath('//*[@id="Zoom"]/descendant::p[1]/img[1]/@src')[0].extract()
        yield item