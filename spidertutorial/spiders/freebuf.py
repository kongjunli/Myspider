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


class Crawl(Spider):
    name = 'freebuf1'
    download_delay = 2
    allowed_domain = ['freebuf.com']
    start_urls = [
       'http://www.freebuf.com/articles/system/page/5'
    ]

    def parse(self, response):
        # 实例化item
        sel = Selector(response)
        item = SpidertutorialItem()
        #self.log('debug info url=' % response.url)
        # 增加title,content,tags tags取当前位置最后一层//html/body/div[5]/div[1]/div[2]/ul[1]/li[12]/div/div[1]/div/span/span
        for i in range(1,10):
            item['title']=sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/dl/dt/a/text()').extract()[i]
            item['summary']=sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/dl/dd[2]/text()').extract()[i]
            item['author']=sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/dl/dd[1]/span[1]/a/text()').extract()[i]
            item['category']=sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/span[1]/a/text()').extract()[i]
            item['pub_time']=sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/dl/dd[1]/span[3]/text()').extract()[i]
            item['scan']=sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/span[2]/strong[1]/text()').extract()[i]
            yield item


        """
        tags="".join(sel.xpath("/html/body/div[4]/div[1]/div[5]/span[@class='tags']/a/text()|/html/body/div[2]/div/div[1]/div[2]/div[2]/div/ul[2]/li/a/@href").extract())
        item['tags']=tags
        yield item
"""
        ###
        # 获得下一篇文章的
        urls = sel.xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/a/@href').extract()
        for url in urls:
            print url
            # url = "https://www.easyaq.com/news/" + url
            yield Request(url, callback=self.parse)











