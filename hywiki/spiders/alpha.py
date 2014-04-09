from scrapy.spider import Spider
from scrapy.selector import Selector

from hywiki.items import HyWord

class HywikiSpider(Spider):
  name = 'alpha'
  allowed_domains = ['hy.wikipedia.org']
  start_urls = [
    'https://hy.wikipedia.org/wiki/Գլխավոր_էջ'
  ]

  def parse(self, response):
    sel = Selector(response)
