import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.adventurehimalayacircuit.com/everest-base-camp-trek.html','https://www.adventurehimalayacircuit.com/everest-kalapathar-trekking.html',
      'https://www.adventurehimalayacircuit.com/everest-panorama-trek.html','https://www.adventurehimalayacircuit.com/everest-base-camp-trek-via-gokyo-lake.html',
      'https://www.adventurehimalayacircuit.com/gokyo-lake-trek.html','https://www.adventurehimalayacircuit.com/everest-base-camp-heli-trek.html',
      'https://www.adventurehimalayacircuit.com/annapurna-circuit-trek.html','https://www.adventurehimalayacircuit.com/annapurna-base-camp-trek.html',
      'https://www.adventurehimalayacircuit.com/ghorepani-poon-hill-trek.html','https://www.adventurehimalayacircuit.com/upper-mustang-trek.html',
      'https://www.adventurehimalayacircuit.com/mardi-himal-trek.html','https://www.adventurehimalayacircuit.com/langtang-valley-trekking.html',
      'https://www.adventurehimalayacircuit.com/manaslu-circuit-trek.html']

for url in urls:

    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')



    Trek=soup.find('h1',{"itemprop":'name'}).find('span')
    head=Trek.decompose()
    trek=soup.find('h1',{"itemprop":'name'}).text.strip()
    time=soup.find('div',{"class":'trip-info'}).find_all('div',{"class":'col-md-6 trip-info_text'})[3].find_all('span')[1].text.strip()
    cost=soup.find('div',{"class":'trip-info'}).find_all('div',{"class":'col-md-6 trip-info_text'})[1].find_all('span')[1].text.strip()
    trip_grade=soup.find('div',{"class":'trip-info'}).find_all('div',{"class":'col-md-6 trip-info_text'})[4].find_all('span')[1].text.strip()
    altitude=soup.find('div',{"class":'trip-info'}).find_all('div',{"class":'col-md-6 trip-info_text'})[5].find_all('span')[1].text.strip()
    contact_or_book_your_trip='https://www.himalayanglacier.com'
    data={
        'Trek':trek,
        'Cost':cost,
        'Time':time,
        'Trip Grade':trip_grade,
        "Max Altitude":altitude,
        'Contact or Book your Trip':contact_or_book_your_trip
        }
    datalist.append(data)
df=pd.DataFrame(datalist)
df.to_csv('adventure.csv',index=True)