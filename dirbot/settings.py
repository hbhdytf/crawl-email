# -*-coding:utf-8-*-
# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1}

#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
        'dirbot.spiders.ua.RotateUserAgentMiddleware' :400,
#        'dirbot.spiders.fake_ua.RandomUserAgentMiddleware' :400,
    }
