import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.adventurehimalayacircuit.com/everest-base-camp-trek.html']
   

for url in urls:

    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')



    Trek=soup.find('h1',{"itemprop":'name'}).find('span')
    head=Trek.decompose()
    trek=soup.find('h1',{"itemprop":'name'}).text.strip()
    time=soup.find('div',{"class":'trip-info'}).find_all('div',{"class":'col-md-6 trip-info_text'})[3].find_all('span')[1].text.strip()
    #time=soup.find('h1',{"class":'tourmaster-single-header-title'}).find('span').text.strip()
    #cost=soup.find('div',{"class":'price'}).find("p").text.strip()
    #trip_grade=soup.find('span',{"class":'hg-tooltip-text'}).text.strip()
    #altitude=soup.find('div',{"class":'col-sm-12 col-md-12 col-lg-12 col-xl-12 tab-overview'}).find_all('div',{"class":'txt-info'})[5].find('span').text.strip()
    contact_or_book_your_trip='https://www.himalayanglacier.com'
    data={
        'Trek':trek,
        #'Cost':cost,
        'Time':time,
        #'Trip Grade':trip_grade,
        #"Max Altitude":altitude,
        'Contact or Book your Trip':contact_or_book_your_trip
        }
    datalist.append(data)
df=pd.DataFrame(datalist)
df.to_csv('adventure.csv',index=True)