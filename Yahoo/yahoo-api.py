#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import warnings
import urllib.parse
import json
import sys
import bz2


# # Yahoo超級商城

# In[2]:


#儲存所有爬下來的資料
def save_meta(entry, soup):
    
    price = entry.select('.BaseGridItem__price___31jkj')[0].text.split("起")[0]
    
    return{
        'title': entry.select('.BaseGridItem__title___2HWui')[0].text,
        'price': price.split('$')[1],
#         'shop': soup.select_one('.uh__ylogoLink___1byk0').text
    } 


def get_data_yahoo():
    
    count = 0
    i = 1
    yahoo = {}
    
    url = "https://tw.search.mall.yahoo.com/search/mall/product?p=%E7%9C%9F%E7%9A%AE%E5%8C%85"
    url_first = url
    
    while(i<11):
        url = requests.get(url)
        soup = BeautifulSoup(url.text)
        clean = soup.select('.BaseGridItem__itemInfo___3E5Bx')
        
        for item in clean:
            meta = save_meta(item, soup)
            yahoo[count] = meta
            count+=1
        
        #get page
        clean_page = soup.select_one('.Pagination__arrowBtn___2ihnp.Pagination__icoArrowRight___2KprV.Pagination__hideArrowOnMobile___2HsbF.Pagination__button___fFc6Y')
        link = clean_page['href']
        url = urllib.parse.urljoin(url_first, str(link))
        
        i+=1
        
    return yahoo


# In[18]:


# yahoo = get_data_yahoo()


# # Yahoo購物中心

# In[11]:


#儲存所有爬下來的資料
def save_meta(entry, soup):
    
    price = entry.select('.BaseGridItem__price___31jkj')[0].text.split("起")[0]
    
    return{
        'title': entry.select('.BaseGridItem__title___2HWui')[0].text,
        'price': price.split('$')[1]
    }  


def get_data_yahooshop():
    
    count = 0
    yahoo = {}
    i = 1
    
#     url = "https://tw.buy.yahoo.com/search/product?p={}".format(str(key))
    url = "https://tw.buy.yahoo.com/search/product?p=真皮包"
    url_first = url
    
    while(i<16):
        url = requests.get(url)
        soup = BeautifulSoup(url.text)
        clean = soup.select('.BaseGridItem__itemInfo___3E5Bx')
        
        for item in clean:
            meta = save_meta(item, soup)
            yahoo[count] = meta
            count+=1
        
        #get page
        clean_page = soup.select_one('.Pagination__arrowBtn___2ihnp.Pagination__icoArrowRight___2KprV.Pagination__hideArrowOnMobile___2HsbF.Pagination__button___fFc6Y')
        link = clean_page['href']
        url = urllib.parse.urljoin(url_first, str(link))
        
        i+=1
        
    return yahoo


# In[17]:


# yahooshop = get_data_yahooshop()
# get_data_yahooshop('皮包')


# In[16]:


# result = {
#     'yahoo超級商城': yahoo,
#     'yahoo購物中心': yahooshop
# }

# json = json.dumps(result ,ensure_ascii=False)

# print(str(json))
# sys.stdout.flush()


# In[ ]:


import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

# test data

yahoo_shop = get_data_yahooshop()
yahoo = get_data_yahoo()

yahoo_all = [yahoo_shop, yahoo]


@app.route('/', methods=['GET'])
def home():
    return jsonify(yahoo_all)


# @app.route('/yahoo/all', methods=['GET'])
# def yahoo_all():
#     return jsonify(cities)


app.run()

