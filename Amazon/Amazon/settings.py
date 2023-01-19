BOT_NAME = 'Amazon'
SPIDER_MODULES = ['Amazon.spiders']
NEWSPIDER_MODULE = 'Amazon.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'image / avif, image / webp, * / *',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep - alive',
    'DNT': '1',
    'Host': 'www.amazon.com',
    'Referer': 'https://www.amazon.com/Python-Crash-Course-2nd-Edition/product-reviews/1593279280/',
    'Sec - Fetch - Dest': 'image',
    'Sec - Fetch - Mode': 'no - cors',
    'TE': 'trailers'
}

FEED_EXPORT_FIELDS = ['customer_name', 'rating', 'review_title', 'review_date', 'review_text']
ROBOTSTXT_OBEY = True
FEEDS = {
    'data/%(name)s/%(name)s_%(time)s.csv':{'format': 'csv'},
    'data/%(name)s/%(name)s_%(time)s.json': {'format': 'json'}
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
