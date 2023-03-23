import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.himalayanglacier.com/trips/annapurna-base-camp-trek/','https://www.himalayanglacier.com/trips/everest-base-camp-trek-for-youths/',
      'https://www.himalayanglacier.com/trips/everest-base-camp-short-trek/','https://www.himalayanglacier.com/trips/everest-base-camp-trek/',
      'https://www.himalayanglacier.com/trips/annapurna-circuit-trek/','https://www.himalayanglacier.com/trips/everest-base-camp-luxury-lodge-trek/',
      'https://www.himalayanglacier.com/trips/everest-base-camp-trek-via-gokyo-lakes/','https://www.himalayanglacier.com/trips/upper-mustang-trek/',
      'https://www.himalayanglacier.com/trips/everest-advanced-base-camp-trek-from-tibet/','https://www.himalayanglacier.com/trips/gokyo-lakes-and-gokyo-ri-trek/',
      'https://www.himalayanglacier.com/trips/mardi-himal-trek/','https://www.himalayanglacier.com/trips/manaslu-circuit-trek/',
      'https://www.himalayanglacier.com/trips/langtang-valley-trek/','https://www.himalayanglacier.com/trips/annapurna-sanctuary-trek/',
      'https://www.himalayanglacier.com/trips/rara-lake-trek/','https://www.himalayanglacier.com/trips/everest-high-passes-trek/',
      'https://www.himalayanglacier.com/trips/kanchenjunga-circuit-trek/','https://www.himalayanglacier.com/trips/everest-view-trek/',
      'https://www.himalayanglacier.com/trips/tsum-valley-trek/','https://www.himalayanglacier.com/trips/the-royal-trek/',
      'https://www.himalayanglacier.com/trips/makalu-base-camp-trek/','https://www.himalayanglacier.com/trips/langtang-gosainkunda-and-helambu-trek/',
      'https://www.himalayanglacier.com/trips/nar-phu-valley-trek/','https://www.himalayanglacier.com/trips/annapurna-circle-trek/',
      'https://www.himalayanglacier.com/trips/everest-kangshung-face-trek/','https://www.himalayanglacier.com/trips/tsum-valley-and-manaslu-trek/',
      'https://www.himalayanglacier.com/trips/khopra-ridge-community-trek/','https://www.himalayanglacier.com/trips/nepal-experience-tour/',
      'https://www.himalayanglacier.com/trips/annapurna-circuit-trek-with-tilicho-lake-and-poon-hill/','https://www.himalayanglacier.com/trips/annapurna-with-tilicho-lake-trek/',
      'https://www.himalayanglacier.com/trips/langtang-valley-trek-with-ganja-la-pass/','https://www.himalayanglacier.com/trips/tamang-heritage-trek/',
      'https://www.himalayanglacier.com/trips/manaslu-and-annapurna-trek-with-tilicho-lake/','https://www.himalayanglacier.com/trips/nepal-trekking-and-everest-himalaya-heli-tour/',
      'https://www.himalayanglacier.com/trips/nepal-hiking-and-culture-tour/','https://www.himalayanglacier.com/trips/annapurna-sunrise-and-everest-view-trek/',
      'https://www.himalayanglacier.com/trips/tenzing-hillary-everest-marathon/']
   

for url in urls:

    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')



    Trek=soup.find('h1',{"class":'tourmaster-single-header-title'}).text.strip()
    time=soup.find('h1',{"class":'tourmaster-single-header-title'}).find('span').text.strip()
    cost=soup.find('div',{"class":'price'}).find("p").text.strip()
    trip_grade=soup.find('span',{"class":'hg-tooltip-text'}).text.strip()
    altitude=soup.find('div',{"class":'col-sm-12 col-md-12 col-lg-12 col-xl-12 tab-overview'}).find_all('div',{"class":'txt-info'})[5].find('span').text.strip()
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