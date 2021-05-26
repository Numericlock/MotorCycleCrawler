import scrapy
from motorcycle_crawler.items import MotorcycleNamesItem

class MotorcycleNameSpiderSpider(scrapy.Spider):
    name = 'motorcycle_name_spider'
    allowed_domains = ['www.bikebros.co.jp']
    start_urls = ['https://www.bikebros.co.jp/catalog/1/']
    def parse(self, response):
        bike_name = response.css('a.bikemaker-name span::text').extract()
        link = response.css('a.bikemaker-name::attr(href)').extract()
#       yield MotorcycleNamesItem(
#            link= response.url,
#            name= response.css('div.contenst h2::text').extract_first(),
#        )
        for i in range(len(bike_name)):
            print(bike_name[i])
            yield MotorcycleNamesItem(
                link='https://www.bikebros.co.jp'+link[i],
                name=bike_name[i],
            )
        path = response.url.replace('https://www.bikebros.co.jp/catalog/', '')
        ids = path.split('/')
        brand_id = ids[0]
        print( response.status)
        if int(brand_id) < 51:
            brand_id = int(brand_id) + 1
            next_link = 'https://www.bikebros.co.jp/catalog/'+str(brand_id)+'/'
            yield scrapy.Request(next_link, callback=self.parse)
