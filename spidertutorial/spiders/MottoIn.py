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

class Crawl(Spider):
    name = 'mottoin'
    download_delay= 1.5
    allowed_domain = ['mottoin.com']
    start_urls = [
        'http://www.mottoin.com/'
    ]

    def parse(self, response):
        # 实例化item
        sel = Selector(response)
        item = SpidertutorialItem()
        #self.log('debug info url='%response.url)
        #增加title,content,tags tags取当前位置最后一层//html/body/div[5]/div[1]/div[2]/ul[1]/li[12]/div/div[1]/div/span/span
        for i in range(1,8):
            item['title'] = sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/div[2]/h2/a/text()').extract()[i]
            item['summary'] = sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/div[2]/div[1]/p/text()').extract()[i]
            item['author'] = sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/div[2]/div[2]/div/a[2]/text()').extract()[i]
            item['category'] = sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/div[1]/a[2]/text()').extract()[i]
            value = "".join(sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/div[2]/div[2]/span[1]/text()').extract()[i])

            item['scan']=filter(str.isdigit,"".join(sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/div[2]/div[2]/span[2]/text()').extract()[i]).encode('utf-8'))
            yield item
        ###

        # 获得下一篇文章的
        urls = sel.xpath('/html/body/div/div[1]/div/div[2]/ul/li/a/@href').extract()
        for url in urls:
            print url
            # url = "https://www.easyaq.com/news/" + url
            yield Request(url, callback=self.parse)











