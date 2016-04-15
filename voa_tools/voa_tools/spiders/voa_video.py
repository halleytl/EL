from time import sleep

from scrapy import Selector
from scrapy.spider import Spider
import scrapy
import json
from voa_tools.items import VoaVideoItem

class VoaVideoSpider(Spider):
    name = "voa_video"
    allowed_domains = ["voanews.com"]
    start_urls = [
        "http://learningenglish.voanews.com"
    ]

    def parse(self, response):
        sel = Selector(response)
        url = sel.xpath('//div[@data-vr-zone="Word of the Day"]//h3/a/@href').extract()[0]
        yield scrapy.Request(response.urljoin(url), self.parser_video_list)

    def parser_video_list(self, response):
        sel = Selector(response)
        for post_href in sel.xpath('//div[@class="list"]//a/@href').extract():
            yield scrapy.Request(response.urljoin(post_href), self.parser_video)
        prev = sel.xpath('//span[@class="prev"]/a/@href').extract()[0]
        sleep(2)
        print "start", response.urljoin(prev)
        yield scrapy.Request(response.urljoin(prev), self.parser_video_list)

    def parser_video(self, response):
        item = VoaVideoItem()
        sel = Selector(response)
        page_main =  response.url.replace(self.start_urls[0], "").split("/")[1]
        word = None
        if page_main == "content":
            word = sel.xpath('//div[@class="articleContent"]//div[@class="j_qtext"]/h2/text()').extract()[0]
        elif page_main == "media":
            word = sel.xpath('//h1[@class="media_title"]/text()').extract()[0].replace(r"\r\n", "").strip()
        else:
            pass
        item["word"] = word
        item["video_desc"] = page_main
        videos_json = sel.xpath('//div[@class="html5PlayerPrimary"]/video/@data-sources').extract()[0]
        for video in json.loads(videos_json):
            item["video_css_class"] = video["CssClass"]
            item["video_src"] = video["Src"]
            item["video_type"]= video["Type"]
            yield item




