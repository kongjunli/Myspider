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
    name = 'secpulse'
    download_delay= 1.5
    allowed_domain = ['secpulse.com']
    start_urls = [
        'https://www.secpulse.com/archives/category/articles/code-audit'
    ]

    def parse(self, response):
        # 实例化item
        sel = Selector(response)
        item = SpidertutorialItem()
        #self.log('debug info url='%response.url)
        #增加title,content,tags tags取当前位置最后一层//html/body/div[5]/div[1]/div[2]/ul[1]/li[12]/div/div[1]/div/span/span
        for i in range(1,6):
            item['title'] = sel.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div/div[1]/p[1]/a/text()').extract()[i]
            item['summary'] = sel.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div/div[1]/p[2]/text()').extract()[i]
            item['author'] = sel.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div/div[1]/div/a[2]/span/text()').extract()[i]
            item['category'] = sel.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div/div[1]/div/a[1]/text()').extract()[i]
            item['pub_time']=re.findall('\d{4}-\d{1,2}-\d{1,2}',sel.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div/div[1]/div/span/span/text()').extract()[4])
            item['scan']=filter(str.isdigit,"".join(sel.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div/div[2]/a[1]/p[1]/text()').extract()[i]).encode('utf-8'))
            yield item
        ###

        # 获得下一篇文章的
        urls = sel.xpath('/html/body/div[4]/div[1]/div[3]/button/@pageurl').extract()
        for url in urls:
            print url
            # url = "https://www.easyaq.com/news/" + url
            yield Request(url, callback=self.parse)











