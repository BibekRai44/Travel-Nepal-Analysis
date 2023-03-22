import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]
urls=['https://www.himalayanglacier.com/trips/nepal/activities/trekking-and-hiking/']
   

for url in urls:

    response=requests.get(url)
    html_content=response.content

    soup=BeautifulSoup(html_content,'html.parser')

    post_divs=soup.find_all("div", {"class": "col-sm-12 col-md-12 col-lg-12 col-xl-12"})

    for post_div in post_divs:
        Trek=post_div.find('div',{"class":'card-body'}).find('h4').text.strip()
        #time=post_div.find('span',{"class":'duration'}).find("i").text.strip()
        #cost=post_div.find('div',{"class":'price'}).find("p").text.strip()
        contact_or_book_your_trip='https://www.himalayanglacier.com'
        data={
            'Trek':Trek,
            #'Cost':cost,
            #'Time':time,
            'Contact or Book your Trip':contact_or_book_your_trip
        }
        datalist.append(data)
df=pd.DataFrame(datalist)
df.to_csv('himalayanglacier.csv',index=True)