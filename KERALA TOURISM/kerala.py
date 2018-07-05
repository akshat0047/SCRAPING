from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
from pandas import ExcelWriter
agency=[]
agency_link=[]
address=[]
phone=[]
mobile=[]
email=[]

for page in range(ord("A"),ord("Z")+1):
    data=requests.get("http://tradekerala.in/category_search.php?cid=4539&char="+chr(page))
    soup=BeautifulSoup(data.text,"lxml")
    for x in soup.find_all("div",{"class":"card-row-inner"}):
       rb=x.find("div",{"class":"card-row-body"})
       agency_link.append("".join(("http://tradekerala.in/",rb.h2.a["href"])))
       agency.append(rb.h2.a.b.text)
       address.append(rb.div.p.text)
       rp=x.find("div",{"class":"card-row-properties"})
       i=0
       for y in rp.dl.find_all("dt"):
         if(i==0):
            phone.append(y.text)
            i=i+1
         elif(i==1):
            mobile.append(y.text)
            i=i+1
         elif(i==2):
            email.append(y.text)
            i=i+1


a={"AGENCY":agency,"WEBSITE":agency_link,"ADDRESS":address,"PHONE":phone,"MOBILE":mobile,"EMAIL":email}
df = pd.DataFrame.from_dict(a, orient='index')



writer=ExcelWriter("link3.xlsx")
df.transpose().to_excel(writer,"sheet5")
writer.save()

df.transpose().to_csv("link3.csv")
