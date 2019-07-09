import scrapy
import time
out_file = open("data.tsv",mode="w",encoding="utf-8")

class YoulaiSpider(scrapy.Spider):
    name = "youlai"
    allowed_domains = ["www.youlai.cn"]
    start_urls = [
        "https://www.youlai.cn/ask",
    ]

    def start_requests(self):
        for i in range(700000,800000):
            url = self.start_urls[0]+"/"+str(i)+".html"
            # print(url)
            # print("停顿1秒...............")
            time.sleep(1)

            requests = scrapy.Request(url,
                                      callback=self.sub_parse)
            yield requests


    def sub_parse(self, response):
        # print(response.url + " !!!")
        question = response.xpath('/html/body/div[2]/div[1]/dl/dt/h3/text()').extract_first(
            default='未爬到')
        answer = response.xpath('/html/body/div[2]/div[1]/div/div[2]/p/text()').extract_first(
            default='未爬到')
        # print(question)
        # print(answer)
        if question!="未爬到" and answer!="未爬到":
            out_file.write(question+"|||"+answer)
            out_file.write("\n")
            out_file.flush()
