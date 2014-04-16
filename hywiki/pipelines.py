import json
from collections import Counter


class HywikiJSONPipeline(object):
  def __init__(self):
    self.num_items = 0
    self.count = Counter()
    self.denominator = 10

  def dump_json(self):
    with open('items-%d.json' % self.num_items, 'w') as outfile:
      json.dump(self.count, outfile)

  def process_item(self, item, spider):
    if item['text'] == '-':
      return
    self.count += Counter(item['text'])
    self.num_items = len(self.count)
    if self.denominator < 1000 and self.num_items / self.denominator > 1:
      self.denominator = 10 * self.denominator
    if self.num_items % self.denominator == 0:
      self.dump_json()
    return item
