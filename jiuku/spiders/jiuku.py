from scrapy import Request
from ..items import *
import random
import json,time
import re

class JiukuSpider(scrapy.Spider):
    name = 'jiuku'
    # start_urls = ['http://www.9ku.com/laoge/500shou.htm']
    start_urls = ['http://www.9ku.com/music/t_m_hits.htm']
    allowed_domains = ['9ku.com']

    def parse(self, response):
        listSong = response.xpath("//div[contains(@class, 'songList')]//ol//li/input/@value").extract()
        item = JiukuItem()
        for i in listSong:
            urls = 'http://www.9ku.com/html/playjs/%s/%s.js' % (i[:3], i[:-1])
            lrc = "http://www.9ku.com/play/%s.htm" % i[:-1]
            item['url'] = urls
            item['lrc'] =lrc
            yield Request(url=item['url'], callback=self.parse_mp3, meta={'item': item})
            # res = requests.get(paly, headers=headers).text
            # html = etree.HTML(res)
            # text = html.xpath("//*[@id='lrc_content']/text()")
            # print(text[0])
    def parse_mp3(self, response):
       item = response.meta['item']
       res = response.text
       mp3list = json.loads(res[1:-1:])
       item['songName'] = mp3list['mname']
       item['UserName'] = mp3list['singer']
       item['mp3'] = mp3list['wma']
       item['pic'] = mp3list['gspic']
       yield item
       # print(item['lrc'])
    #
    #    yield Request(url=item['lrc'], callback=self.parse_mp3, meta={'item': item})
    #
    # def parse_lrc(self, response):
    #     item = response.meta['item']
    #     lrc = response.xpath("//*[@id='lrc_content']/text()")
    #     print(response.text)



