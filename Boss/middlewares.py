# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.conf import settings
import requests
import datetime
import random

class BossSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BossDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# class BossProxyIPDownloaderMiddleware(object):
#     def __init__(self,ip=''):
#         self.ip=ip
#
#     def process_request(self,spider,request):
#         # proxy_list = ['125.105.49.122:16152', '111.179.173.102:15751', '117.43.1.219:15726', '114.232.43.234:23892', '114.231.153.1:20186', '183.15.123.254:15887', '1.195.150.208:15861', '101.206.234.112:23613', '223.151.114.189:19022', '42.57.110.17:22869', '101.132.146.133:23353', '58.52.52.97:17715', '223.241.1.162:16075', '123.188.198.229:23487', '1.198.89.128:16129', '60.162.244.205:16536', '125.119.180.73:23311', '192.144.149.110:23257', '27.158.127.155:22344', '183.166.145.178:23657', '220.249.149.120:15452', '116.209.102.50:18592', '118.190.148.167:15527', '125.126.196.202:20452', '175.7.199.140:16087', '125.112.194.144:19031', '110.17.187.166:22345', '171.13.148.225:21601', '113.58.233.252:21990', '114.97.243.210:16584', '221.234.195.210:15369', '117.57.23.71:21363', '1.195.226.38:16933']
#         proxy = settings['DAILI_IP']
#         # proxy = random.choice(proxy_list)
#         # print('*'*50)
#         # print(str(proxy))
#         request.meta['proxy'] = proxy

class BossProxyIPDownloaderMiddleware(object):
    def __init__(self):
        # self.url='http://api.ip.data5u.com/dynamic/get.html?order=70901931a34f53fce375b78c015a31be&sep=3'
        self.url='http://api.ip.data5u.com/dynamic/get.html?order=87655ad5892132392c6309339fd8356b&sep=3'
        self.proxy = ''
        self.expire_datetime = datetime.datetime.now() - datetime.timedelta(minutes=1)
        # self._get_proxyip()

    def _get_proxyip(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }
        self.proxy = requests.get(self.url,headers=headers).text
        print(self.proxy)
        self.expire_datetime = datetime.datetime.now() + datetime.timedelta(minutes=0.5) # 代理过期时间

    def _check_expire(self):
        if datetime.datetime.now() >= self.expire_datetime: # 判断当前时间是否大于过期时间
            self._get_proxyip()
            # print('*'*50)
            # print(self.proxy)

    def process_request(self,spider,request):
        self._check_expire()
        request.meta['proxy'] = 'http://' + self.proxy
