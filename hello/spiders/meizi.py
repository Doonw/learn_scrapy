# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com/a/more_1.html']

    def __init__(self):
        self.time = datetime.now().timestamp()

    # @property
    # def running(self):
    #     return datetime.now().timestamp() - self.time < 3 * 60

    def parse(self, response):
        for item in response.css("li.wp-item h3.tit > a ::attr(href)").extract():
            if item:
                yield scrapy.Request(url=item, callback=self.detail)
        for i in response.css("div#wp_page_numbers ul li a"):
            if '下一页' == i.css("*::text").extract_first():
                next_page = i.css("*::attr(href)").extract_first();
                if next_page:
                    self.log("next page: %s" % next_page)
                    yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def detail(self, response):
        title = response.css('title::text').extract_first();
        yield {
            "title": title[:-6] if title else "NoneTitle",
            'image_urls':response.css("div#picture p img::attr(src)").extract(),
        }

