# -*- coding: utf-8 -*-
import scrapy
from Boss.items import BossItem


class JobClassSpider(scrapy.Spider):
    name = 'job_class'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/gongsi/_zzz_t802/']

    def parse(self, response):
        company_list = response.xpath('//div[@class="company-tab-box company-list"]/ul/li')
        for comp in company_list:
            item = BossItem()
            item['come_from'] = 'job_class'
            item['company'] = comp.xpath('./div[@class="sub-li"]//div[@class="conpany-text"]/h4/text()').extract_first()
            item['company_url'] ='https://www.zhipin.com/gongsir/' + comp.xpath('./div[@class="sub-li"]/a/@href').extract_first()[8:]
            url = item['company_url'] + '?page=1&ka=page-1'
            yield scrapy.Request(url=url,callback=self.company_parse_1,meta={'item':item})

        url_1 = response.xpath('//div[@class="company-tab-box company-list"]/div[@class="page"]/a[last()]/@href').extract_first()
        url_2 = response.xpath('//div[@class="company-tab-box company-list"]/div[@class="page"]/a[last()]/@ka').extract_first()
        if url_1 != 'javascript:;':
            next_url = 'https://www.zhipin.com'+url_1+'&ka='+url_2
            yield  scrapy.Request(url=next_url,callback=self.parse)


    def company_parse_1(self, response):
        item = response.meta['item']
        jobs_class_info = response.xpath('//ul[contains(@class,"filter-list") and @id="filter-job"]/div[@class="filter-list-content"]/li')
        for j in jobs_class_info[1:]:
            job_class = j.xpath('./a/text()').extract_first()
            n1 = job_class.find('(')
            n2 = job_class.rfind(')')
            item['job_classification'] = job_class[:n1 - 1]
            item['job_class_number'] = job_class[n1 + 1:n2]
            # print(item)
            yield item
