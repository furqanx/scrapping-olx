import scrapy


class BigdataspiderSpider(scrapy.Spider):
    name = "bigdataspider"
    allowed_domains = ["www.olx.co.id"]
    start_urls = ["https://www.olx.co.id/motor-bekas_c200"]

    def parse(self, response):
        products = response.xpath('//li/a/div[contains(@class, "fTZT3")]')
        for product in products:
            yield{
                'brand' : product.css('span._2poNJ::text').get(),
                'lokasi' : product.css('span._2VQu4::text').get(),
                'tahun' : product.css('span.YBbhy::text').get(),
                'harga' : product.css('span._2Ks63::text').get()
            }
