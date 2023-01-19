from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import Item, ItemLoader

import scrapy


def clean_reviews(param:str):
    return param.split(' ')[0]

def clean_date(param:str):
    return param.split(' ')[-3:]


class AmazonItem(Item):
    customer_name = scrapy.Field()
    rating = scrapy.Field()
    review_title = scrapy.Field()
    review_date = scrapy.Field()
    review_text = scrapy.Field()


class AmazonItemLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    rating_in = MapCompose(clean_reviews)
    review_date_in = MapCompose(clean_date)
