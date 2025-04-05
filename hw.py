#this app scrape data from booking.com
"""
give the url,file name
greetings
start scraping,
hotel name,
price,
location
reviws
link
save the file


"""

import requests
from bs4 import BeautifulSoup as bs
import lxml
import csv


url_text='https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi%2C+India&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Aq73wr8GwAIB0gIkMzE0ODY0OTEtNTRhOS00ZTI2LWI4MzQtOTQ0MzllZjZmZTI42AIF4AIB&sid=da37e465ce5570e651695d00c645131c&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&checkin=2025-04-11&checkout=2025-05-13&group_adults=2&no_rooms=1&group_children=0'

header = {'User-Agent' :
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}

response = requests.get(url_text,headers=header)



if response.status_code == 200:
    print('All good!')
    html_content=response.text
    #creating soup
    soup = bs(html_content,'lxml')
    
    hotel_divs = soup.find_all('div',role="listitem")
    
    with open('hotels.csv','w') as file_csv:
        writer = csv.writer(file_csv)
        #adding header
        writer.writerow(['Hotel name', 'location', 'price', 'rating', 'review', 'link'])

        
        for hotel in hotel_divs:
            
            hotel_name = hotel.find('div' , class_ ="f6431b446c a15b38c233").text.strip()
            hotel_location = hotel.find('span',class_ = "aee5343fdb def9bc142a").text.strip()
            hotel_price = hotel.find('span',class_="f6431b446c fbfd7c1165 e84eb96b1f").text.strip().replace('₹ ','')
        
            rating = hotel.find('div', class_="a3b8729ab1 d86cee9b25")
            
            if rating:
                hotel_rating =  rating.text.strip().split(' ')[-1]
            else:
                hotel_rating='N/A'
                
                
            review = hotel.find('div',class_="a3b8729ab1 e6208ee469 cb2cbb3ccb")
            if review:
                hotel_review = review.text.strip()
            else:
                hotel_review='N/A'
            
            #getting link
            hotel_link = hotel.find('a',href=True).get('href')
            
            #saving the file to csv
            writer.writerow([hotel_name,hotel_location,hotel_price,hotel_rating,hotel_review,hotel_link])
        
    
    for hotel in hotel_divs:
        hotel_name = hotel.find('div' , class_ ="f6431b446c a15b38c233").text.strip()
        hotel_location = hotel.find('span',class_ = "aee5343fdb def9bc142a").text.strip()
        hotel_price = hotel.find('span',class_="f6431b446c fbfd7c1165 e84eb96b1f").text.strip().replace('₹ ','')
        
        rating = hotel.find('div', class_="a3b8729ab1 d86cee9b25")
        if rating:
           hotel_rating =  rating.text.strip().split(' ')[-1]
        else:
            hotel_rating='N/A'
        review = hotel.find('div',class_="a3b8729ab1 e6208ee469 cb2cbb3ccb")
        if review:
            hotel_review = review.text.strip()
        else:
            hotel_review='N/A'
            
        #getting link
        hotel_link = hotel.find('a',href=True).get('href')
        
        
        print(hotel_name)
        print(hotel_location)
        print(hotel_price)
        print(hotel_rating)
        print(hotel_review)
        print(hotel_link)
        
        print('')
        
    
    
    
else:
    print(f'error :{response.status_code}')
    





