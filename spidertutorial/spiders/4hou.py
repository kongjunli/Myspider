# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:19:39 2017

@author: kjl
"""
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from spidertutorial.items import SpidertutorialItem
import re
import math
import datetime
class Crawl(Spider):
    name ='4hou'
    download_delay= 1.5
    allowed_domain = ['4hou.com']
    start_urls = [
        'http://www.4hou.com/page'
    ]

    def parse(self, response):
        # 实例化item
        sel = Selector(response)
        item = SpidertutorialItem()
        #self.log('debug info url='%response.url)
        #增加title,content,tags tags取当前位置最后一层//html/body/div[5]/div[1]/div[2]/ul[1]/li[12]/div/div[1]/div/span/span
        for i in range(1,3):
            item['title'] = sel.xpath('/html/body/div[2]/section/article[1]/div/li/div/a/h1/text()').extract()[i]
            item['summary'] = sel.xpath('/html/body/div[2]/section/article[1]/div/li/div/p/text()').extract()[i]
            item['author'] = sel.xpath('/html/body/div[2]/section/article[1]/div/li/div/div[1]/a/p/text()').extract()[i]
            item['category'] = sel.xpath('/html/body/div[2]/section/article[1]/div/div[1]/div/li/a/div/span/text()').extract()[i]
            value ="".join(sel.xpath('/html/body/div[2]/section/article[1]/div/div[1]/div/li/div/div[2]/p/text()').extract()[i])
            aa=datetime.datetime.strptime(value,'%Y年%m月%d日')
            item['pub_time']=aa.strftime('%Y-%m-%d')

            item['scan']=filter(str.isdigit,"".join(sel.xpath('/html/body/div[2]/section/article[1]/div/div[1]/div/li/div/div[2]/div/div[1]/span/text()').extract()[i]).encode('utf-8'))
            yield item
        ###

        # 获得下一篇文章的
        urls = sel.xpath('/html/body/div[2]/section/article[1]/div/div[2]/a/@href').extract()
        for url in urls:
            print url
            # url = "https://www.easyaq.com/news/" + url
            yield Request(url, callback=self.parse)











