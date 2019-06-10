# -*- coding: utf-8 -*-

# Scrapy settings for Boss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

BOT_NAME = 'Boss'

SPIDER_MODULES = ['Boss.spiders']
NEWSPIDER_MODULE = 'Boss.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.randint(10,30)
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
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
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Boss.middlewares.BossSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'Boss.middlewares.BossDownloaderMiddleware': 543,
#     'Boss.middlewares.BossProxyIPDownloaderMiddleware':120,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Boss.pipelines.BossPipeline1': 300,
    # 'Boss.pipelines.BossPipeline2': 400,
    # 'Boss.pipelines.BossPipeline3': 500,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = 'rm-2ze32iuz58i1leh7e9o.mysql.rds.aliyuncs.com'
MYSQL_USER = 'scc'
MYSQL_DATABASE = 'cube_online'
MYSQL_PASSWORD = 'Cube1234'

# MYSQL_HOST = 'localhost'
# MYSQL_USER = 'root'
# MYSQL_DATABASE = 'boss_data'
# MYSQL_PASSWORD = '12345'

DAILI_IP = 'http://' + '116.255.189.171:16816'
