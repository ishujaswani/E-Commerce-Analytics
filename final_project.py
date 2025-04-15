#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:09:20 2022

@author: ishujaswani
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def review_count_scraper():
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = 'https://www.amazon.in/gp/bestsellers/garden/ref=zg_bs_nav_0/258-0752277-9771203'
    
    response=requests.get(url,headers=headers)
    print(response.status_code)
    
    
    soup=BeautifulSoup(response.content,'lxml')
    
    
    Name = []
    Lower_Price = []
    Upper_Price = []
    Ratings = []
    Reviews = []
    
    reviews = soup.find_all('a',class_='a-size-small a-link-normal')
    for k in reviews:
         Reviews.append(k.text)
    
    for item in soup.select('.zg-item-immersion'):
        try:
            Name.append(item.select('.p13n-sc-truncate')[0].get_text().strip())
        except Exception as e:
            #raise e
            Name.append('NA')
    
    for item in soup.select('.zg-item-immersion'):
        try:
            Lower_Price.append(item.select('.p13n-sc-price')[0].get_text().strip())
        except Exception as e:
            #raise e
            Lower_Price.append('NA')
    for item in soup.select('.zg-item-immersion'):
        try:
            Upper_Price.append(item.select('.p13n-sc-price')[1].get_text().strip())
        except Exception as e:
            #raise e
            Upper_Price.append('NA')
    for item in soup.select('.zg-item-immersion'):
        try:
            Ratings.append(item.select('.a-icon-alt')[0].get_text().strip())
        except Exception as e:
            #raise e
            Ratings.append('NA')
            
    df = pd.DataFrame(list(zip(Name,Lower_Price,Upper_Price,Ratings,Reviews)))
    df.columns = ['Names','Lower Price', 'Upper Price', 'Ratings','Reviews Count']
    print(df)
    
    # File_name = 'Amazom_Garden_Data.xlsx'
    df.to_excel('/Users/ishujaswani/Documents/Amazom_Garden_Data.xlsx')
    print('Data is written to excel successfully')
    
    time.sleep(60)
    
end_timer = time.time() + 60 * 1
while time.time() < end_timer:
    review_count_scraper()