import scrapy


class MoviescrapSpider(scrapy.Spider):
    name = 'moviescrap'
    allowed_domains = ['rezka.ag']
    start_urls = ['https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html']

    def parse(self, response):

        title= response.xpath(
            "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[1]/h1").extract()
        original_title = response.xpath(
            '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[2]').extract()
        imdb = response.xpath(
            "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[1]/td[2]/span[1]/span").extract()
        country = response.xpath(
            "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[5]/td[2]/a").extract()
        duration = response.xpath(
            '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[10]/td[2]').extract()
        description = response.xpath(
            '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[5]/div[2]').extract()

        row_data = zip(title, original_title, imdb, country, duration, description)

        for item in row_data:
            scraped_info={
                'title': item[0],
                'original_title': item[1]
                'imdb': item[2],
                'country': item[3],
                'duration': item[4],
                "description": item[5]
            }
            yield scraped_info
