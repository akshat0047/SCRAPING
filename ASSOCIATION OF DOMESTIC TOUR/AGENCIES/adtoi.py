from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import ExcelWriter

data=requests.get("http://www.adtoi.in/member-list.php")
soup=BeautifulSoup(data.text,"lxml")

i=0
agency=[]
address=[]

rows= soup.find_all("tr")

for r in rows:
    i=0
    for f in r.find_all("td"):
        if(i==0):
            agency.append(f.a["href"].split("=",2)[2])
            i=i+1
        else:
            address.append(" ".join(f.text.split()))


a={"AGENCY":agency,"ADDRESS":address}
df = pd.DataFrame.from_dict(a, orient='index')



writer=ExcelWriter("aset.xlsx")
df.transpose().to_excel(writer,"sheet5")
writer.save()

df.transpose().to_csv("aset.csv")

