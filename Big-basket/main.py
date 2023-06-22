import time
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from csv import DictWriter
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://www.bigbasket.com/")
driver.maximize_window() # fullscreen
time.sleep(3)

action = ActionChains(driver)

# Hovering through Shop by category button
element = driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[1]/a')
action.move_to_element(element).perform()

for i in range(1, 6):
    category_1 = driver.find_element(By.XPATH, '//*[@id="navBarMegaNav"]/li['+str(i)+']/a')
    action.move_to_element(category_1).perform()
    
    print("CATEGORY1", category_1.text)
    j = 1
    while True:
        try: 
            category_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/div/div/ul/li[1]/ul/li/mega-nav-template/div/div/div/left-subcategory-template/div/div/div/div[1]/ul/li['+str(j)+']/a') 
            print("CATEGORY2", category_2.text)
            action.move_to_element(category_2).perform()
            k = 1
            while True:
                try:
                    category_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/div/div/ul/li[1]/ul/li/mega-nav-template/div/div/div/left-subcategory-template/div/div/div/div[2]/div/div/div/div[1]/div/ul/li['+str(k)+']/a')
                    print("CATEGORY3", category_3.text)
                    action.move_to_element(category_3).click().perform()
                    # for i in range(10):
                    #     product = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div[2]')
                    #     print("PRODUCT************", product.text)
                    k = k + 1
                except:
                    break
            
            j = j + 1
        except:
            break 
    

driver.close()



