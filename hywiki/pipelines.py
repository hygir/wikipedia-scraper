import json
from collections import defaultdict


class HywikiJSONPipeline(object):
  def __init__(self):
    self.num_items = 0
    self.items = defaultdict(int)
    self.denominator = 10
    self.already_dumped_counts = set()

  def dump_json(self, prefix=''):
    if self.num_items in self.already_dumped_counts:
      return
    with open('%sitems-%d.json' % (prefix, self.num_items), 'w') as outfile:
      json.dump(self.items, outfile, indent=2)
      self.already_dumped_counts.add(self.num_items)

  def process_item(self, item, spider):
    self.items[item['text']] += 1
    self.num_items = len(self.items)
    if self.denominator < 10000 and self.num_items / self.denominator > 1:
      self.denominator = 10 * self.denominator
    if self.num_items % self.denominator == 0:
      self.dump_json(prefix=spider.name + '-')
    return item

  def close_spider(self, spider):
    self.dump_json(prefix=spider.name + '-')
