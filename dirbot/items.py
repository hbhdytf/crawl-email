from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    email = Field()
    url = Field()
