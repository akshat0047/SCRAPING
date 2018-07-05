import scrapy
from scrapy.loader import ItemLoader 
from kerala.items import KeralaItem,Contacts

class Spider(scrapy.Spider):
    name="tourism"
    
    def start_requests(self):
      print("start")
      url="http://www.iato.in/members/lists"
      yield scrapy.Request(url,self.parse)
      print("yield")
    
    def parse(self,response):
            I=ItemLoader(item=KeralaItem(),response=response)
            I.add_xpath("AGENCY","//table[1]/tbody//tr//td[2]/a/text()")
            data1=response.xpath("//table[1]/tbody//tr//td[2]/a/@href").extract()
           
            I.add_xpath("ADDRESS","//table[1]/tbody//tr//td[3]/text()")
            for link in data1:
              request=response.follow(str(link),self.parse_enter) 
              yield request

            yield I.load_item()

    def parse_enter(self,response):
       C=ItemLoader(item=Contacts(),response=response)
       print("im running")  
       C.add_xpath("ABOUT","//div[@class='post-content'][1]/div/text()")
       C.add_xpath("SPECIALIZATION","//div[@class='post-content'][2]/div/text()")
       C.add_xpath("BRIEF","//div[@class='post-content'][3]/div/text()")
       print("done")
      
       C.add_xpath("CONTACT_PERSON","//div[@class='post-content'][4]//p[2]/text()")
       C.add_xpath("DESIGNATION","//div[@class='post-content'][4]//p[3]/text()")
       C.add_xpath("STREET_ADDRESS","//div[@class='post-content'][4]//p[4]/text()")
       C.add_xpath("EMAIL","//div[@class='post-content'][4]//p[8]/text()")
       C.add_xpath("PHONE","//div[@class='post-content'][4]//p[9]/text()")
       C.add_xpath("MOBILE","//div[@class='post-content'][4]//p[10]/text()")
       C.add_xpath("WEBSITE","//div[@class='post-content'][4]//p[11]/text()")
       yield C.load_item()
       
       
       





