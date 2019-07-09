import scrapy
import time

class YoulaiSpider(scrapy.Spider):
    name = "youlai"
    allowed_domains = ["www.youlai.cn"]
    start_urls = [
        "https://www.youlai.cn/ask",
    ]

    def start_requests(self):
        for i in range(700000,800000):
            url = self.start_urls[0]+"/"+str(i)+".html"
            print(url)
            print("停顿1秒...............")
            time.sleep(1)

            requests = scrapy.Request(url,
                                      callback=self.sub_parse)
            yield requests


    def sub_parse(self, response):
        print(response.url + " !!!")
        # print(response.body)
        print("!!!!")

