import scrapy

class SimpleSpider(scrapy.Spider):
    name = "simple"
    start_urls = ['https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=4821987857866231335&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9210541&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1']

    def parse(self, response):
        for item in response.css('h2::text'):  # Adjust this selector as needed
            yield {'Details ': item.get()}

            #RUN THIS COMMANDS IN THE TERMINAL FOR GET DATA
            #scrapy runspider flips.py
            #scrapy runspider flips.py -o flips.csv