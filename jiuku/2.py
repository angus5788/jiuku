import re
import requests
from lxml import etree

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDU_SSP_lcr=https://www.google.com/; Hm_lvt_a5de315acb973b8e6da83458c9e456d3=1602063408; tt=ok; cc=ok; __gads=ID=d5accb32e915af08:T=1602063411:S=ALNI_MZnlbpQrjbCGjDU3eNhhDvCqpiQBg; tmp_addplay=; pp=ok; jpvolume=0.321; shows=no; ff=no; jk_ifplay=1; Hm_lpvt_a5de315acb973b8e6da83458c9e456d3=1602064263; l_music=877087/875689/1002010/995478/1006548/1004197/1005157l_end; jk_addplay=877087/995478/1005157/1004197/1006548/998378/1007153/1003659/996722/1003604/994287/1003669/1003606/1007258/1001166/875689/994784/1003605/997050/875595/860301/1008282/1002010/1006078/1006094/999604/1006311/1002493/891238/1000663/1005876/890196/65937/11417/30001/59930/1903/1000452/464446/82151/649/663208/471298/473312/186947/600306/998626/',
    'Host': 'www.9ku.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}


def get():
    url = "https://www.9ku.com/douyin/bang.htm"
    res = requests.get(url).text
    # html = etree.HTML(res)
    # value =html.xpath("//div[@class='Mbox-bd']/div[contains(@class, 'musicList')]//li/input/@value")
    # listSong =html.xpath("//div[contains(@class, 'songList')]//ol//li/input/@value")
    a = re.compile('<a target="(.*?)" href="(.*?)" class="songName ">(.*?)</a>')
    listSong = a.findall(res)

    for i in listSong:
        #     urls = 'http://www.9ku.com/html/playjs/%s/%s.js' % (i[:3], i[:-1])
        paly = "http://www.9ku.com/%s" % (i[1])
        res = requests.get(paly, headers=headers).text
        content = re.compile('<meta property="og:title" content="(.*?)"/>')
        name = content.findall(res)
        html = etree.HTML(res)
        text = html.xpath("//*[@id='lrc_content']/text()")
        print(text[0])


if __name__ == "__main__":
    get()
