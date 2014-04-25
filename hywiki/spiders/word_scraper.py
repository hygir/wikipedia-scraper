# coding=utf-8
from hywiki.items import HyWord
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import Selector


class HywikiWordSpider(CrawlSpider):
  name = 'word_scraper'
  allowed_domains = ['hy.wikipedia.org']
  start_urls = [
    'https://hy.wikipedia.org/wiki/Գլխավոր_էջ'
  ]
  rules = (
    #Rule(SgmlLinkExtractor(allow=['https://hy.wikipedia.org/.*'])),
    Rule(SgmlLinkExtractor(allow=['https://hy.wikipedia.org/wiki/[^:#]*$']),
         'parse_word',
         follow=True),
  )

  word_regex_text = u'[\u0561-\u0586\u0531-\u0556]+[\u0561-\u0586\u0531-\u0556\-]+'

  def parse_word(self, response):
    sel = Selector(response)
    page_contents = sel.xpath('//*[@id="mw-content-text"]')

    for content in page_contents:
      for match in content.re(self.word_regex_text):
        word = HyWord()
        word['text'] = match.lower()
        yield word
