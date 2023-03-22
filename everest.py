import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.nepalhikingteam.com/package/everest-base-camp-trek/','https://www.nepalhikingteam.com/package/everest-base-camp-short-trek/',
      'https://www.nepalhikingteam.com/package/everest-base-camp-heli-shuttle-trek/','https://www.nepalhikingteam.com/package/everest-base-camp-heli-trek/',
      'https://www.nepalhikingteam.com/package/everest-base-camp-trek-for-seniors-and-kids/','https://www.nepalhikingteam.com/package/everest-chola-pass-trek/',
      'https://www.nepalhikingteam.com/package/everest-gokyo-lake-renjo-la-pass-trek/','https://www.nepalhikingteam.com/package/everest-high-passes-trek/',
      'https://www.nepalhikingteam.com/package/short-everest-trek/','https://www.nepalhikingteam.com/package/everest-panorama-trek/','https://www.nepalhikingteam.com/package/everest-view-trek/',
      'https://www.nepalhikingteam.com/package/luxury-everest-base-camp-heli-trek/','https://www.nepalhikingteam.com/package/everest-base-camp-trek-with-chola-and-renjo-la-passes/']
   

for url in urls:

    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')

    post_divs=soup.find_all("section", {"class": "package-formation"})

    for post_div in post_divs:
        Trek=post_div.find('div',{"class":'col xs-12 sm-12 md-8'}).find('h1').text.strip()
        time=post_div.find('ul',{"class":'package-meta'}).find("li").text.strip()
        cost=post_div.find('div',{"class":'feature-trip-price'}).text.strip()
        trip_grade=post_div.find('ul',{"class":'facts-list'}).find('li').find("dd").text.strip()
        altitude=post_div.find('ul',{"class":'facts-list'}).find_all('li')[1].find("dd").text.strip()
        accomodation=post_div.find('ul',{"class":'facts-list'}).find_all('li')[4].find("dd").text.strip()
        best_travel_time=post_div.find('ul',{"class":'facts-list'}).find_all('li')[5].find("dd").text.strip()
        data={
            'Trek':Trek,
            'Cost':cost,
            'Time':time,
            'Trip Grade':trip_grade,
            'Max Altitude':altitude,
            'Accomodation':accomodation,
            'Best Travel Time':best_travel_time
        }
        datalist.append(data)
df=pd.DataFrame(datalist)
df.to_csv('Data.csv',index=True)