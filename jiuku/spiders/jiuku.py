import json,os
from ..items import *
from scrapy.utils.project import get_project_settings


class JiukuSpider(scrapy.Spider):
    def __init__(self):
        settings = get_project_settings().get("FILES_STORE")
        if not os.path.exists(settings):
            os.makedirs(settings)

    name = 'jiuku'
    # start_urls = ['http://www.9ku.com/laoge/500shou.htm']
    # start_urls = ['http://www.9ku.com/music/t_m_hits.htm']
    start_urls = ['https://www.9ku.com/douyin/bang.htm']
    allowed_domains = ['9ku.com']

    def parse(self, response):
        listSong = response.xpath("//div[contains(@class, 'songList')]//ol//li/input/@value").extract()
        item = JiukuItem()
        for i in listSong:
            urls = "https://www.9ku.com/playlist.php"
            item['url'] = urls
            item['lrc'] = "https://www.9ku.com/downlrc.php?id=%s" % i[:-1]
            data = {
                'ids': "%s" % i[:-1]
            }
            yield scrapy.Request(url=item['lrc'], meta={"id": i[:-1]}, callback=self.parse_Lrc)
            yield scrapy.FormRequest(url=item['url'], callback=self.parse_mp3, formdata=data)

    def parse_Lrc(self, response):
        url = "https://www.9ku.com/play/%s.htm" % response.meta['id']
        yield scrapy.Request(url=url, callback=self.dwonload_Lrc)

    def dwonload_Lrc(self, response):
        settings = get_project_settings().get("FILES_STORE")

        title = response.xpath("/html/head/title/text()").get()
        s = title.find("在")
        SongNmae = title[:s:]
        with open('%s%s.lrc' % (settings, SongNmae), 'w+') as f:
            f.write(response.text)

    def parse_mp3(self, response):
        item = response.meta
        res = response.text
        mp3list = json.loads(res[1:-1:])
        item['songName'] = mp3list['mname']
        item['UserName'] = mp3list['singer']
        item['mp3'] = mp3list['wma']
        item['pic'] = mp3list['gspic']

        yield item
