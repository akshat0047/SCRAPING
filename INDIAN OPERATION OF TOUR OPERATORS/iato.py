from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
from pandas import ExcelWriter
NAME=[]
ADDRESS=[]

data=requests.get("http://www.iato.in/members/lists")
soup=BeautifulSoup(data.text,"lxml")

for x in soup.tbody.find_all("tr"):
    i=0
    for y in x.find_all("td"):
        i=i+1
        if(i==2):
            NAME.append(y.a.text)
        elif(i==3):
            ADDRESS.append(y.text)

b={"NAME":NAME,"ADDRESS":ADDRESS}
df=pd.DataFrame.from_dict(b,orient="index")
writer=ExcelWriter("link4.xlsx")
df.transpose().to_excel(writer,"sheet5")
writer.save()

df.transpose().to_csv("link4.csv")

            
        
