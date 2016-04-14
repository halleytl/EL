from scrapy.spider import Spider

class VoaVideoSpider(Spider):
    name = "voa_video"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://learningenglish.voanews.com/archive/word-of-the-day/"

    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)