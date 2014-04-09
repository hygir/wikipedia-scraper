# Scrapy settings for hywiki project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hywiki'

SPIDER_MODULES = ['hywiki.spiders']
NEWSPIDER_MODULE = 'hywiki.spiders'

DEPTH_LIMIT = 1

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hywiki (+http://www.yourdomain.com)'
