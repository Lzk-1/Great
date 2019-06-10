# -*- coding: utf-8 -*-
import scrapy
from Boss.items import BossItem
import time
import requests
from lxml import etree
import random


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/gongsi/_zzz_t802/']

    def parse(self, response):
        headers = {
            'authority': 'www.zhipin.com',
            'method': 'GET',
            'path': '/gongsi/_zzz_t802/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'lastCity=101010100; _uab_collina=155730649362280515200272; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1559033502,1559182767,1559529656,1560130654; __c=1560130654; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; __a=82788545.1557306493.1559529656.1560130654.321.18.3.321; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1560130672',
            'referer': 'https://www.zhipin.com/gongsi/?ka=header_brand',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'
        }

        company_list = response.xpath('//div[@class="company-tab-box company-list"]/ul/li')
        for comp in company_list:
            item = BossItem()
            item['come_from'] = 'job'
            # item['date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            item['company'] = comp.xpath('./div[@class="sub-li"]//div[@class="conpany-text"]/h4/text()').extract_first()
            item['company_url'] ='https://www.zhipin.com/gongsir/' + comp.xpath('./div[@class="sub-li"]/a/@href').extract_first()[8:]
            url_0 = item['company_url'] + '?page=1&ka=page-1'
            response1 = requests.get(url_0,headers=headers).text
            response1 = etree.HTML(response1)
            count = response1.xpath('//div[@class="tab-wrap"]/ul[@class="tabs"]/li[2]/a/text()')[0][5:-1]
            n = int(int(count)/15) + 1
            if n>30:
                n = 30

            i = 1
            while i < n:
                url = item['company_url'] + '?page={0}&ka=page-{1}'.format(str(i), str(i))
                i += 1
                yield scrapy.Request(url=url,callback=self.job_parse,meta={'item':item})

            t1 = random.randint(10,20)
            time.sleep(t1)

        url_1 = response.xpath('//div[@class="company-tab-box company-list"]/div[@class="page"]/a[last()]/@href').extract_first()
        url_2 = response.xpath('//div[@class="company-tab-box company-list"]/div[@class="page"]/a[last()]/@ka').extract_first()
        if url_1 != 'javascript:;':
            next_url = 'https://www.zhipin.com'+url_1+'&ka='+url_2
            yield  scrapy.Request(url=next_url,callback=self.parse)


    def job_parse(self, response):
        item = response.meta['item']
        # a = response.xpath('//div[@class="intro-basis"]//div[@class="body-con"]/text()').extract_first()
        # n1 = a.find('·')
        # n2 = a.rfind('·')
        # item['scale'] = a[:n1-1]
        # item['status'] = a[n1+2:n2-1]
        # item['kind'] = a[n2+2:]
        # item['job_update_time'] = response.xpath('//div[@class="basis-body"]/div[@class="update-time"]/text()').extract_first()[:10]
        # item['job_number'] = response.xpath('//div[@class="tab-wrap"]/ul[@class="tabs"]/li[2]/a/text()').extract_first()[5:-1]
        jobs = response.xpath('//ul[@class="position-list"]/li')
        for temp in jobs:
            item['job'] = temp.xpath('./a[@class="a-link"]/h4/text()').extract()[0].strip()
            item['salary'] = temp.xpath('./a[@class="a-link"]/h4/span[@class="price"]/text()').extract_first()
            item['work_place'] = temp.xpath('./a[@class="a-link"]/div/text()').extract()[0].strip()
            item['experience'] = temp.xpath('./a[@class="a-link"]/div/text()').extract()[1].strip()
            item['education'] = temp.xpath('./a[@class="a-link"]/div/text()').extract()[2].strip()
            # print(item)
            yield item
