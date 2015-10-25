__author__ = 'yangtengfei'
from scrapy import cmdline
#cmdline.execute("scrapy crawl ustc --logfile=log -s JOBDIR=crawl/ustc".split())
cmdline.execute("scrapy crawl ustc --logfile=log -s".split())
