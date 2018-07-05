from selenium import webdriver

from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import ExcelWriter

data=requests.get("http://www.adtoi.in/member-list.php")
soup=BeautifulSoup(data.text,"lxml")

agency=[]
address=[]
contact_person=[]
mobile=[]
website=[]
telephone=[]
website=[]
email=[]
fax=[]
ABOUT=[]
SPECIALIZATION=[]

rows= soup.table.tbody.find_all("tr")
for x in rows:
   i=0
   for f in x.find_all("td"):
        if(i==0):
            agency.append(f.a["href"].split("=",2)[2])
            link="http://www.adtoi.in/"+f.a["href"]
            data1=requests.get(link)
            print(data1.status_code)
                     
            
         
            soup1=BeautifulSoup(data1.text,"xml")
            j=1

            print(soup1.xpath("//div[class='inclusions'][1]//h4[1]/text()"))
            