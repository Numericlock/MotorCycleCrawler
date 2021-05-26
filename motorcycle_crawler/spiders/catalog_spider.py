import scrapy
import requests
from motorcycle_crawler.items import MotorcycleCrawlerItem

class CatalogSpiderSpider(scrapy.Spider):
    name = 'catalog_spider'
    allowed_domains = ['www.bikebros.co.jp','api.burl=ikebros.co.jp']
    start_urls = ['https://www.bikebros.co.jp/catalog/1/7_37/']

    def parse(self, response):
        th = response.css('div#bike_model_info th::text').extract()
        td = response.css('div#bike_model_info td::text').extract()
        bike_model = response.css('a.bike_model::attr(data-bike_model_id)').extract()
        print(bike_model)
        url = 'https://api.burl=ikebros.co.jp/v1/bike//bike_model_detail.jsonp?bike_model_id='+bike_model[0]
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Host": "httpbin.org",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
            "X-Amzn-Trace-Id": "Root=1-5ee7bae0-82260c065baf5ad7f0b3a3e3"
        }
        res = requests.get(url, headers=headers)
        pprint("????????????")
        pprint(res.json())
        data = res.json()
        print(data)
        #for i in range(len(th)):
        #    match = td[i].replace('\t', '')
        #    match = match.replace('\n', '')
        #    print(match)
        #    yield MotorcycleCrawlerItem(
        #        url=response.url,
        #        th=th[i],
        #        td=match,
        #    )

