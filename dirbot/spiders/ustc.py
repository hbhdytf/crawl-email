import re
import sys

from scrapy.spiders import *
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from dirbot.items import Website

reload(sys)
sys.setdefaultencoding('utf-8')


class UstcSpider(CrawlSpider):
    name = "ustc"
    allowed_domains = ["ustc.edu.cn"]
    start_urls = [
        "http://www.ustc.edu.cn/"
    ]
    rules = [
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        email = []
        others = re.findall(
            r'[\w]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*(?:\sAT\s|\sat\s|\[at\]|\(at\)|@|#)ustc.edu.cn',
            response.body,
            re.S
        )
        for other in others:
            reg = re.compile(r'(?:\sAT\s|\sat\s|\[at\]|\(at\)|#)')
            email.append(reg.sub('@', other))
        print email
        item = Website()
        item["name"] = sel.xpath('/html/head/title/text()').extract()[0]
        item["url"] = response.url
        item["email"] = email
        return item
