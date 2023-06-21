import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from csv import DictWriter

driver = webdriver.Chrome()
driver.get("https://food.grab.com/ph/en/restaurants") # resturants in Manila
driver.maximize_window() # fullscreen

time.sleep(3)
scroll_pause_time = 5
field_names = ['title', 'longitude', "latitude"]
screen_height = driver.execute_script("return window.screen.height;") 
i = 1.0
driver.execute_script("window.scrollTo(0, {screen_height}*1);".format(screen_height=screen_height, i=i))
i = i + 1

# scrolling infinitely throughout the screen
for i in range(2):
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i = i + 1.5
    data = driver.find_element("id", "__NEXT_DATA__").get_attribute("innerHTML")
    parsed_data = json.loads(data)
    
    restaurants_list = parsed_data["props"]["initialReduxState"]["pageRestaurantsV2"]["entities"]["restaurantList"]
    
    for key in restaurants_list: 
        restaurant = {}
        restaurant["title"] = restaurants_list[key]["name"]
        restaurant["longitude"] = restaurants_list[key]["longitude"]
        restaurant["latitude"] = restaurants_list[key]["latitude"]
        
        df = pd.DataFrame(restaurant,index=[0])
        
        with open('event.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(restaurant)
            f_object.close()
        
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height)*i > scroll_height:
        break 
    
    time.sleep(scroll_pause_time) # wait time after each scroll

df = pd.read_csv('event.csv')
df = df.drop_duplicates()
df.to_csv('ans.csv', header=False, index=False)

driver.close()
    