import scrapy


class LightparsnewSpider(scrapy.Spider):
    name = "lightparsnew"
    allowed_domains = ["svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/svetilniki-potolochnye"]

    def parse(self, response):
        lights = response.css('li.item')

        for light in lights:
            yield {
                'name': light.css('a').attrib['title'],
                'url': light.css('a').attrib['href'],
                'price': light.css('span.pprice::text').get()
            }
