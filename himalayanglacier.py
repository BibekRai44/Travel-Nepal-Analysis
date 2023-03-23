import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.himalayanglacier.com/trips/annapurna-base-camp-trek/']
   

for url in urls:

    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')



    Trek=soup.find('h1',{"class":'tourmaster-single-header-title'}).text.strip()
    time=soup.find('h1',{"class":'tourmaster-single-header-title'}).find('span').text.strip()
    cost=soup.find('div',{"class":'price'}).find("p").text.strip()
    trip_grade=soup.find('span',{"class":'hg-tooltip-text'}).text.strip()
    altitude=soup.find('div',{"class":'div.col-sm-12.col-md-12.col-lg-12.col-xl-12.overview-block.p-0'}).find('div',{"class":'txt-info'})[5].find_all('span').text.strip()
    contact_or_book_your_trip='https://www.himalayanglacier.com'
    data={
        'Trek':Trek.split("-")[0],
        'Cost':cost,
        'Time':time.removeprefix("-"),
        'Trip Grade':trip_grade,
        "Max Altitude":altitude,
        'Contact or Book your Trip':contact_or_book_your_trip
        }
    datalist.append(data)
df=pd.DataFrame(datalist)
df.to_csv('himalayanglacier.csv',index=True)