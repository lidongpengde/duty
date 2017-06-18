# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DutyItem(scrapy.Item):
	interfaceName = scrapy.Field()
	total = scrapy.Field()
	average = scrapy.Field()
	line = scrapy.Field()
	qps = scrapy.Field()
