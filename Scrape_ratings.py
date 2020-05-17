
# coding: utf-8

#%%
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

os.chdir('/Users/Ricci/Desktop/Scrapy')

#%%
#extract country names
url = 'https://countryeconomy.com/ratings/moodys'

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers=kv, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("Scrape Failed")
    
    
html=r.text
soup = BeautifulSoup(html, "html.parser")

countrylist = soup.find_all('div',{'class':'col-sm-12'})[0] 
country_link = countrylist.find_all('a')
countrylink = pd.DataFrame(columns=['countrylink'])
for i in range(0,len(country_link)):
    clink = country_link[i].get('href')  
    countrylink = countrylink.append({'countrylink':clink},ignore_index=True)  
    
#%% extract moody's data
    
#column_name = []
#for i in range(1,111):
#    column_name.append('LTFC_Date%s'%i)
#    column_name.append('LTFC_Rating%s'%i)
#    column_name.append('LTLC_Date%s'%i)
#    column_name.append('LTLC_Rating%s'%i)
#    column_name.append('STFC_Date%s'%i)
#    column_name.append('STFC_Rating%s'%i)
#    column_name.append('STLC_Date%s'%i)
#    column_name.append('STLC_Rating%s'%i)
column_name = []
column_name.append('LTFC_Date')
column_name.append('LTFC_Rating')
column_name.append('LTLC_Date')
column_name.append('LTLC_Rating')
column_name.append('STFC_Date')
column_name.append('STFC_Rating')
column_name.append('STLC_Date')
column_name.append('STLC_Rating')
output_moody = pd.DataFrame(columns=column_name)

#output_moody = output_moody.iloc[:1003,]

#for loop for each country
for i in range(1,len(countrylink)+1):
    url = 'https://countryeconomy.com/'+str(countrylink.iloc[i-1,0])
 
#    kv = {'user-agent':'Mozilla/5.0'}
#    r = requests.get(url, headers=kv, timeout=30)
#    r.raise_for_status()
#    r.encoding = r.apparent_encoding
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html=r.text
        soup = BeautifulSoup(html, "html.parser")
    
        clist_moody = soup.find_all('div',{'class':'tab-pane fade in active'})
        content_moody = clist_moody[0].find_all('td')
        for j in range(0,int(len(content_moody)/8)):
            LTFC_Date = content_moody[j*8].get_text()
            LTFC_Rating = content_moody[j*8+1].get_text()
            LTLC_Date = content_moody[j*8+2].get_text() 
            LTLC_Rating = content_moody[j*8+3].get_text() 
            STFC_Date = content_moody[j*8+4].get_text() 
            STFC_Rating = content_moody[j*8+5].get_text() 
            STLC_Date = content_moody[j*8+6].get_text() 
            STLC_Rating = content_moody[j*8+7].get_text() 
            output_moody = output_moody.append(pd.DataFrame({'idx':i,'LTFC_Date':[LTFC_Date], 'LTFC_Rating':[LTFC_Rating], 'LTLC_Date':[LTLC_Date], 'LTLC_Rating':[LTLC_Rating], 'STFC_Date':[STFC_Date],'STFC_Rating':[STFC_Rating],'STLC_Date':[STLC_Date],'STLC_Rating':[STLC_Rating]}), ignore_index=True)

    except:
        break
        print("Scrape Failed")

#%% extract S&P data
column_name = []
column_name.append('LTFC_Date')
column_name.append('LTFC_Rating')
column_name.append('LTLC_Date')
column_name.append('LTLC_Rating')
column_name.append('STFC_Date')
column_name.append('STFC_Rating')
column_name.append('STLC_Date')
column_name.append('STLC_Rating')
output_sp = pd.DataFrame(columns=column_name)

for i in range(1,len(countrylink)+1):
    url = 'https://countryeconomy.com/'+str(countrylink.iloc[i-1,0])
 
#    kv = {'user-agent':'Mozilla/5.0'}
#    r = requests.get(url, headers=kv, timeout=30)
#    r.raise_for_status()
#    r.encoding = r.apparent_encoding
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html=r.text
        soup = BeautifulSoup(html, "html.parser")
          
        clists_sp = soup.find_all('div',{'class':'tab-pane fade in','id':'sp'})
        content_sp = clists_sp[0].find_all('td')
        for j in range(0,int(len(content_sp)/8)):
            LTFC_Date = content_sp[j*8].get_text()
            LTFC_Rating = content_sp[j*8+1].get_text()
            LTLC_Date = content_sp[j*8+2].get_text() 
            LTLC_Rating = content_sp[j*8+3].get_text() 
            STFC_Date = content_sp[j*8+4].get_text() 
            STFC_Rating = content_sp[j*8+5].get_text() 
            STLC_Date = content_sp[j*8+6].get_text() 
            STLC_Rating = content_sp[j*8+7].get_text() 
            output_sp = output_sp.append(pd.DataFrame({'idx':i, 'LTFC_Date':[LTFC_Date], 'LTFC_Rating':[LTFC_Rating], 'LTLC_Date':[LTLC_Date], 'LTLC_Rating':[LTLC_Rating], 'STFC_Date':[STFC_Date],'STFC_Rating':[STFC_Rating],'STLC_Date':[STLC_Date],'STLC_Rating':[STLC_Rating]}), ignore_index=True)
    except:
        break
        print("Scrape Failed") 
       
#%% extract Fitch data
column_name = []
column_name.append('LTFC_Date')
column_name.append('LTFC_Rating')
column_name.append('LTLC_Date')
column_name.append('LTLC_Rating')
column_name.append('STFC_Date')
column_name.append('STFC_Rating')
column_name.append('STLC_Date')
column_name.append('STLC_Rating')
output_fitch = pd.DataFrame(columns=column_name)

for i in range(1,len(countrylink)+1):
    url = 'https://countryeconomy.com/'+str(countrylink.iloc[i-1,0])
 
#    kv = {'user-agent':'Mozilla/5.0'}
#    r = requests.get(url, headers=kv, timeout=30)
#    r.raise_for_status()
#    r.encoding = r.apparent_encoding
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html=r.text
        soup = BeautifulSoup(html, "html.parser")
        
        clists_fitch = soup.find_all('div',{'class':'tab-pane fade in','id':'fitch'})
        content_fitch = clists_fitch[0].find_all('td')
        for j in range(0,int(len(content_fitch)/8)):
            LTFC_Date = content_fitch[j*8].get_text()
            LTFC_Rating = content_fitch[j*8+1].get_text()
            LTLC_Date = content_fitch[j*8+2].get_text() 
            LTLC_Rating = content_fitch[j*8+3].get_text() 
            STFC_Date = content_fitch[j*8+4].get_text() 
            STFC_Rating = content_fitch[j*8+5].get_text() 
            STLC_Date = content_fitch[j*8+6].get_text() 
            STLC_Rating = content_fitch[j*8+7].get_text() 
            output_fitch = output_fitch.append(pd.DataFrame({'idx':i, 'LTFC_Date':[LTFC_Date], 'LTFC_Rating':[LTFC_Rating], 'LTLC_Date':[LTLC_Date], 'LTLC_Rating':[LTLC_Rating], 'STFC_Date':[STFC_Date],'STFC_Rating':[STFC_Rating],'STLC_Date':[STLC_Date],'STLC_Rating':[STLC_Rating]}), ignore_index=True)
    except:
        break
        print("Scrape Failed")                         
        
#%% output data to files
output_moody = output_moody.set_index('idx')
index_moody=[]
for i in range(0,len(output_moody.index)):
    index_moody.append(int(output_moody.index[i]))
output_moody.index = index_moody
output_moody.to_excel('Moodys Rating.xlsx')

output_sp = output_sp.set_index('idx')
index_sp=[]
for i in range(0,len(output_sp.index)):
    index_sp.append(int(output_sp.index[i]))
output_sp.index = index_sp
output_sp.to_excel('S&P Rating.xlsx') 

output_fitch = output_fitch.set_index('idx')
index_fitch=[]
for i in range(0,len(output_fitch.index)):
    index_fitch.append(int(output_fitch.index[i]))
output_fitch.index = index_fitch
output_fitch.to_excel('Fitch Rating.xlsx') 
