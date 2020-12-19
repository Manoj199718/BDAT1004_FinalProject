import requests as rs
from bs4 import BeautifulSoup
import pandas as pd
from .models import Flipkart,Amazon,Paytm,Snapdeal

def other_products(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for a in soup.findAll('div',attrs={'class':['_3liAhj','_3O0U0u']}):
            try:
                
                price=a.find('div',attrs={'class':['_1vC4OE','_1vC4OE _2rQ-NK']})
                pricef.append(price.string)
                name=a.find('a',attrs={'class':['_2cLu-l','_3wU53n']})
                namesf.append(name.string)
                
            except:
                namesf.append("Name or category error")
                pricef.append("Price error")
        data_list = list(zip(namesf,pricef))[0:5]
        for i in data_list:
            a = Flipkart(name = i[0],price = i[1])
            a.save()
        data1_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Name","Price"])
        
        return data1_table.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)
    
        
def mobile_phones(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for line in soup.findAll('div',attrs={'class':'_2kHMtA'}):
            try:
                names=line.find('div',attrs={'class':'_4rR01T'})
                phone_name=names.string;
                namesf.append(phone_name)
                names2=line.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
                pricef.append(names2.string)   
            except:
                namesf.append("Name or category error")
                pricef.append("Price error")
        data_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Names","Prices"])
        #print("Products in Flipkart Site ")
        #print(data_table.head(5))
        # entries = []
        # for e in data_table.T.to_dict().values():
        #     entries.append(Flipkart(**e))
        # Flipkart.objects.bulk_create(entries)
        data_list = list(zip(namesf,pricef))[0:5]
        for i in data_list:
            a = Flipkart(name = i[0],price = i[1])
            a.save()
        return data_table.head(5)
        print('halo')
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def fashion(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for line in soup.findAll('div',attrs={'class':'_1xHGtK _373qXS'}):
            try:
                names=line.find('a',attrs={'class':'IRpwTa'})
                fashion_name=names.string;
                namesf.append(phone_name)
                names2=line.find('div',attrs={'class':'_30jeq3'})
                pricef.append(names3.string)

            except:
                namesf.append("Name or category error")
                pricef.append("Price error")
        data_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Names","Prices"])
        data_list = list(zip(namesf,pricef))[0:5]
        for i in data_list:
            a = Flipkart(name = i[0],price = i[1])
            a.save()

        return data_table.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def paytm(key):
    try:
        url="https://paytmmall.com/shop/search?q="
        final=url+key
        data=rs.get(final)
        soup=BeautifulSoup(data.text,'html.parser')
        namess=[]
        prices=[]
        for line in soup.findAll('div',attrs={'class':'_1fje'}):
            try:
                names=line.find('div',attrs={'class':'UGUy'})
                namess.append(names.string)
                price=line.find('div',attrs={'class':['_1kMS','dQm2']})
                prices.append(price.span.text)
                
            except:
                namess.append("Name or category error")
                prices.append("Price error")
            
        #print("Items in paytm mall : ")
        #print(data1)
        data1=pd.DataFrame(list(zip(namess,prices)),columns=["Names","Prices"])
        data_list = list(zip(namess,prices))[0:5]
        for i in data_list:
            a = Paytm(name = i[0],price = i[1])
            a.save()
        # entries = []
        # for e in data1.T.to_dict().values():
        #     entries.append(Paytm(**e))
        # Paytm.objects.bulk_create(entries)
        return data1.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def snapdeal(key):
    try:
        url="https://www.shopclues.com/search?q="
        url2="&sc_z=2222&z=0&count=0"
        final=url+key+url2
        data=rs.get(final)
        prices=[]
        namess=[]
        soup=BeautifulSoup(data.text,'html.parser')
        for line in soup.findAll('div',attrs={'class':['column col3 search_blocks','column col3']}):
            try:
                price=line.find('span',attrs={'class':'p_price'})
                prices.append(price.string)
                name=line.find(['span','h2'],attrs={'class':['','prod_name']})
                namess.append(name.string)
                
            except:
                namess.append("Name or category error")
                prices.append("price error")
        #print('Items in Snapdeal site')
        #print(datat.head(5))
        datat=pd.DataFrame(list(zip(namess,prices)),columns=["Names","Prices"])
        entries = []
        data_list = list(zip(namess,prices))[0:5]
        for i in data_list:
            a = Snapdeal(name = i[0],price = i[1])
            a.save()
        # for e in datat.T.to_dict().values():
        #     entries.append(Snapdeal(**e))
        # Snapdeal.objects.bulk_create(entries)
        return datat.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)

def amazon(key):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        url="https://www.amazon.in/s?k="
        url2="&ref=nb_sb_noss_2"
        final=url+key+url2
        data=rs.get(final,headers = headers)
        content = data.content
        prices=[]
        namess=[]
        soup=BeautifulSoup(content,'html.parser')
        #print(soup.title)
        for line in soup.findAll(class_ = 's-include-content-margin s-border-bottom s-latency-cf-section'):
            try:
                price=line.find('span', attrs={'class':'a-offscreen'})
                price_f = str(price).replace('<span class="a-offscreen">','').replace('</span>','')
                prices.append(price_f)
                name=line.find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
                namess.append(name.string)
            except:
                namess.append("Name or category error")
                prices.append("price errorr")
        #print('Items in Snapdeal site')
        #print(datat.head(5))
        print(prices)
        data_list = list(zip(namess,prices))
        print(data_list)
        data_list.pop(0)
        for i in data_list[0:5]:
            a = Amazon(name = i[0],price = i[1])
            a.save()
        datat=pd.DataFrame(data_list,columns=["Names","Prices"])
        
        return datat.head(5)
    except:
        namer=["Name or category error"]
        pricer=["Error"]
        edata=pd.DataFrame(list(zip(namer,pricer)),columns=["Name","Price"])
        return edata.head(1)