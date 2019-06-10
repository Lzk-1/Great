# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    come_from = scrapy.Field()
    # date = scrapy.Field()
    company = scrapy.Field()
    company_url = scrapy.Field()
    scale = scrapy.Field()
    status = scrapy.Field()
    kind = scrapy.Field()
    # tags = scrapy.Field()
    job_update_time = scrapy.Field()
    job_number = scrapy.Field()
    job_classification = scrapy.Field()
    job_class_number = scrapy.Field()
    job = scrapy.Field()
    salary = scrapy.Field()
    work_place = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()

