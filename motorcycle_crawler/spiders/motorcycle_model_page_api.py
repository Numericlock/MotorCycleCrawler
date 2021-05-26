import scrapy
import csv

class MotorcycleModelPageApiSpider(scrapy.Spider):
    name = 'motorcycle_model_page_api'
    allowed_domains = ['www.bikebros.co.jp']
    start_urls = ['https://www.bikebros.co.jp/catalog/1/']

    def __init__(self, *args, **kwargs):
        super(MotorcycleModelPageApiSpider, self).__init__(*args, **kwargs)
        csv_file = open('./url.csv', 'r', encoding="UTF-8", errors="", newline="")
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        scrapurls = []
        for row in f:
            scrapurls.append(row)
        self.start_urls = scrapurls
        print(scrapurls)

    def parse(self, response):
        pass
