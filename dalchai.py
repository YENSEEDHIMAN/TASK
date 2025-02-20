import scrapy

class SimpleSpider(scrapy.Spider):
    name = "simple"
    start_urls = ['https://chaldal.com/fresh-vegetable']

    def parse(self, response):
        for item in response.css('.name::text'):  # Adjust this selector as needed
            yield {'title': item.get()}


            #RUN THIS COMMANDS IN THE TERMINAL FOR GET DATA
            #scrapy runspider dalchai.py
            #scrapy runspider flips.py -o dalchai.csv