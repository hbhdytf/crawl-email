from os import path
import sqlite3

from scrapy.signalmanager import SignalManager
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    filename = 'data.sqlite'

    def __init__(self):
        self.conn = None
        sig=SignalManager(sender=dispatcher.Any)
        sig.connect(self.initialize,signals.engine_started)
        sig.connect(self.finalize, signals.engine_stopped)

    def process_item(self, item, spider):
        for email in item['email']:
            try:
                self.conn.execute('insert into ustc values(?,?,?)',(email, unicode(item['name']), item['url']))
                self.conn.commit()
            except:
                pass
        return item

    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        conn.execute(
            """CREATE TABLE ustc
            (email TEXT PRIMARY KEY, name TEXT, link TEXT)"""
        )
        conn.commit()
        return conn
