# coding=utf-8
from hywiki.items import HyWord
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re


class HywikiUrlSpider(CrawlSpider):
  name = 'url_scraper'
  allowed_domains = ['hy.wikipedia.org']
  start_urls = [
    'https://hy.wikipedia.org/wiki/Գլխավոր_էջ'
  ]
  rules = (
    Rule(SgmlLinkExtractor(allow=['https://hy.wikipedia.org/wiki/[^:#]*$']),
         'parse_word',
         follow=True),
  )

  word_regex = re.compile(
      u'[\u0561-\u0586\u0531-\u0556]+[\u0561-\u0586\u0531-\u0556\-]+')

  def parse_word(self, response):
    word = HyWord()
    word['text'] = response.url
    yield word
