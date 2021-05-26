import scrapy
from motorcycle_crawler.items import MotorcycleCrawlerItem

class CatalogSpiderSpider(scrapy.Spider):
    name = 'catalog_spider'
    allowed_domains = ['www.bikebros.co.jp']
    start_urls = ['https://www.bikebros.co.jp/catalog/1/1_1/']

    def parse(self, response):
        th = response.css('div#bike_model_info th::text').extract()
        td = response.css('div#bike_model_info td::text').extract()
        for i in range(len(th)):
            match = td[i].replace('\t', '')
            match = match.replace('\n', '')
            print(match)
            yield MotorcycleCrawlerItem(
                url=response.url,
                th=th[i],
                td=match,
            )
        path = response.url.replace('https://www.bikebros.co.jp/catalog/', '')
        ids = path.split('/')
        brand_id = ids[0]
        motorcycle_ids = ids[1].split('_')
        motorcycle_id = motorcycle_ids[0]
        model_year_id = motorcycle_ids[1]
        model_year_id = int(model_year_id) + 1
        print( response.status)
        if str(response.status) == "404":
            motorcycle_id = int(motorcycle_id) + 1
            model_year_id = 1
        next_link = 'https://www.bikebros.co.jp/catalog/'+str(brand_id)+'/'+str(motorcycle_id)+'_'+str(model_year_id)+'/'
        yield scrapy.Request(next_link, callback=self.parse)

