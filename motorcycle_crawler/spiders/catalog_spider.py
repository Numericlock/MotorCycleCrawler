import scrapy
import requests
import csv
from motorcycle_crawler.items import MotorcycleCrawlerItem

class CatalogSpiderSpider(scrapy.Spider):
    name = 'catalog_spider'
    allowed_domains = ['www.bikebros.co.jp']
    start_urls = ['https://www.bikebros.co.jp/catalog/1/7_37/']

    def parse(self, response):
        bike_models = response.css('a.bike_model::attr(data-bike_model_id)').extract()
        url = 'https://api.bikebros.co.jp/v1/bike//bike_model_detail.jsonp'
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
        headers = {
            "Host": "api.bikebros.co.jp",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "ja,en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        print(bike_models)
        for id in bike_models:
            params = {'bike_model_id': id}
            res = requests.get(url, headers=headers,params=params)
            print(res)
            time.sleep(3)
            #data = res.text
            #print(data)

