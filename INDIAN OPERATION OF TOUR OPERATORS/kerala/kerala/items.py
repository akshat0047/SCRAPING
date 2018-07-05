# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KeralaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    AGENCY=scrapy.Field()
    ADDRESS=scrapy.Field()
    
    

class Contacts(scrapy.Item):
    ABOUT=scrapy.Field()
    SPECIALIZATION=scrapy.Field()
    BRIEF=scrapy.Field()
    CONTACT_PERSON=scrapy.Field()
    DESIGNATION=scrapy.Field()
    STREET_ADDRESS=scrapy.Field()
    EMAIL=scrapy.Field()
    WEBSITE=scrapy.Field()
    PHONE=scrapy.Field()
    MOBILE=scrapy.Field()

    
    