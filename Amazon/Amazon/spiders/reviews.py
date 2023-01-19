import scrapy
from ..items import AmazonItem, AmazonItemLoader


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['amazon.com']
    start_url = 'https://www.amazon.com/Python-Crash-Course-2nd-Edition/product-reviews/{}/'
    ansi_list = ['1593279280']

    def start_requests(self):
        for asin in self.ansi_list:
            url = self.start_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        review_list = response.xpath('//div[@id="cm_cr-review_list"]//div[contains(@data-hook,"review")]')
        for review in review_list:
            amazon_item = AmazonItemLoader(item=AmazonItem(), selector=review)
            amazon_item.add_xpath('customer_name', './/span[@class="a-profile-name"]/text()')
            amazon_item.add_css('rating', '.review-rating > span::text')
            amazon_item.add_xpath('review_title', './/a[@data-hook="review-title"]/span/text()')
            amazon_item.add_xpath('review_date', './/span[@data-hook="review-date"]/text()')
            amazon_item.add_xpath('review_text', './/span[@data-hook="review-body"]/span/text()')
            yield amazon_item.load_item()

        next_page = response.xpath('//li[@class="a-last"]/a/text()').get()
        if next_page:
            next_url = response.urljoin(response.xpath('//li[@class="a-last"]/a/@href').get())
            yield scrapy.Request(next_url)
