# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.exceptions import DropItem
from  scrapy.pipelines.files import FilesPipeline
# 下载图片
class MyFilesPipeline(FilesPipeline):
    def item_completed(self, results, item, info):
        print(results)
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        return item

    def get_media_requests(self, item, info):
            yield scrapy.Request(item['mp3'],meta={'item':item})

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
