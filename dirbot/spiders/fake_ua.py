# -*-coding:utf-8-*-
__author__ = 'yangtengfei'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from fake_useragent import UserAgent

class RandomUserAgentMiddleware(object):
    def __init__(self):
        super(RandomUserAgentMiddleware, self).__init__()

        self.ua = UserAgent()

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua.random)
        print request.headers