# -*- coding: utf-8 -*-
import scrapy
from Boss.items import BossItem

class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/gongsi/_zzz_t802/']


    def parse(self, response):
        company_list = response.xpath('//div[@class="company-tab-box company-list"]/ul/li')
        for comp in company_list:
            item = BossItem()
            item['come_from'] = 'company'
            item['company'] = comp.xpath('./div[@class="sub-li"]//div[@class="conpany-text"]/h4/text()').extract_first()
            item['company_url'] ='https://www.zhipin.com/gongsir/' + comp.xpath('./div[@class="sub-li"]/a/@href').extract_first()[8:]
            url = item['company_url'] + '?page=1&ka=page-1'
            yield scrapy.Request(url=url,callback=self.company_parse,meta={'item':item})

        url_1 = response.xpath('//div[@class="company-tab-box company-list"]/div[@class="page"]/a[last()]/@href').extract_first()
        url_2 = response.xpath('//div[@class="company-tab-box company-list"]/div[@class="page"]/a[last()]/@ka').extract_first()
        if url_1 != 'javascript:;':
            next_url = 'https://www.zhipin.com'+url_1+'&ka='+url_2
            yield  scrapy.Request(url=next_url,callback=self.parse)


    def company_parse(self, response):
        item = response.meta['item']
        a = response.xpath('//div[@class="intro-basis"]//div[@class="body-con"]/text()').extract_first()
        n1 = a.find('·')
        n2 = a.rfind('·')
        item['scale'] = a[:n1-1]
        item['status'] = a[n1+2:n2-1]
        item['kind'] = a[n2+2:]
        item['job_number'] = response.xpath('//div[@class="tab-wrap"]/ul[@class="tabs"]/li[2]/a/text()').extract_first()[5:-1]
        # print(item)
        yield item









