from bs4 import BeautifulSoup
import requests
import lxml
import requests
import pandas as pd
from pandas import ExcelWriter

r = requests.head("http://attoi.org/members/")
print(r.status_code)

data= requests.get("http://attoi.org/members/")
soup=BeautifulSoup(data.text,"lxml")

NAME=[]
POST=[]
COMPANY_NAME=[]
ADDRESS=[]
PHONE=[]
MAIL=[]
WEBSITE=[]

NAME1=[]
POST1=[]
COMPANY_NAME1=[]
ADDRESS1=[]
PHONE1=[]
MAIL1=[]
WEBSITE1=[]

i=0
j=0
k=0
grid=soup.find_all("div",{"class":"grid"})

#looping through all divs with grid class

for x in grid:
    i=i+1
    if(i==4): #2 div with main members info
        for y in x.find_all("div",{"class":"column span-6"}):
            j=0
            for z in y.div.find_all("div"):
             k=0   
             if(j==0):
                for p in z.find_all("h5"):
                    if(k==0):
                        NAME.append(p.text)
                        k=k+1
                    else:
                        POST.append(p.text)
                        j=j+1
                
                
             else:
                 COMPANY_NAME.append(z.h3.text)
                 for p in z.find_all("h5"):
                     if(k==0):
                         str1=p.text
                         k=k+1
                         
                     elif(k==1):
                         str2=p.text
                         ADDRESS.append(",".join((str1,str2)))
                         k=k+1
                         
                     elif(k==2):
                          str1=p.text
                          k=k+1
                          
                     elif(k==3):
                          str2=p.text
                          PHONE.append(",".join((str1,str2)))
                          k=k+1
                          
                     elif(k==4):
                          MAIL.append(p.text)
                          k=k+1    
                     
                     elif(k==5):
                          str1=p.a["href"]
                          k=k+1
                     elif(k==6):
                          str2=p.a["href"]
                          WEBSITE.append(",".join((str1,str2)))
                          k=1
    elif(i==96):          #4 div with allied members info
         for y in x.find_all("div",attrs={"class":"column span-6"}):
            j=0
            for z in y.div.find_all("div"):
             k=0
             if(j==0):
                for p in z.find_all("h5"):
                     if(k==0):
                          NAME1.append(p.text)
                          k=k+1
                     else:
                          POST1.append(p.text)
                          j=j+1
                
                
             else:
                 COMPANY_NAME1.append(z.h3.text)
                 for p in z.find_all("h5"):
                     if(k==0):
                         str1=p.text
                         k=k+1
                         
                     elif(k==1):
                         str2=p.text
                         ADDRESS1.append(",".join((str1,str2)))
                         k=k+1
                         
                     elif(k==2):
                          str1=p.text
                          k=k+1
                          
                     elif(k==3):
                          str2=p.text
                          PHONE1.append(",".join((str1,str2)))
                          k=k+1
                          
                     elif(k==4):
                           MAIL1.append(p.text)
                           k=k+1
                     elif(k==5):
                           str1=p.a["href"]
                           k=k+1
                     elif(k==6):
                           str2=p.a["href"]
                           WEBSITE1.append(",".join((str1,str2)))
                           k=1
                         
                

a={"NAME":NAME,"POST":POST,"COMPANY NAME":COMPANY_NAME,"ADDRESS":ADDRESS,"PHONE":PHONE,"MAIL":MAIL,"WEBSITE":WEBSITE,"NAME(allied)":NAME1,"POST(allied)":POST1,"COMPANY NAME(allied)":COMPANY_NAME1,"ADDRESS(allied)":ADDRESS1,"PHONE(allied)":PHONE1,"MAIL(allied)":MAIL1,"WEBSITE(allied)":WEBSITE1}
             
df = pd.DataFrame.from_dict(a, orient='index')



writer=ExcelWriter("aset1.xlsx")
df.transpose().to_excel(writer,"sheet5")
writer.save()

df.transpose().to_csv("aset1.csv")
