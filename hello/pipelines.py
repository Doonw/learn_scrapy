# -*- coding: utf-8 -*-
import scrapy

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class HelloPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item.get('image_urls'):
            for i in item['image_urls']:
                yield scrapy.Request(i)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item