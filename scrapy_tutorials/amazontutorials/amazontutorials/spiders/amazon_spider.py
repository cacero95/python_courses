# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialsItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www2.sgc.gov.co/Paginas/servicio-geologico-colombiano.aspx',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ##product_name = response.css('.singleCell , img::attr(src)').extract()
        ##title = response.css('b::text').extract()
        ##yield {
        ##    'product_name':product_name,
        ##    'title': title
        ##}
        img = response.css('.wrapperNoticias picture').getall()
        all_images = response.css('img::attr(src)').getall()
        last_news = response.css('.infoNoticias').extract()
        print('#########')
        print('salida')
        print(img)
        print('salida')
        print('#########')
        yield {'imgs': img, 'all_images':all_images, 'news': last_news}
        ##links = response.css('div.seccionMap li a').xpath('@href').extract()
        ##yield {'links': links}