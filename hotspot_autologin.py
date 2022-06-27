from ast import Return
from pickle import TRUE
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import requests
from requests.adapters import HTTPAdapter
from sqlalchemy import false, true
from urllib3 import Retry
import time
import sys
from pyvirtualdisplay import Display


class Internet():

    def __init__(self, website:str, hotspot:str, username:str) -> None:
        adapter = HTTPAdapter(max_retries=Retry(total=4, 
            backoff_factor=1, 
            allowed_methods=None, 
            status_forcelist=[429, 500, 502, 503, 504]))
        
        self.hotspot = hotspot
        self.username = username
        self.website = website


        self.session = requests.Session()
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers={'Cache-Control': 'no-cache'}
    
    def check_website(self):
        try: 
            r = self.session.get(self.website)
        except:
            return False
        return True

    def check_hotspot(self):
        try: 
            r = self.session.get(self.hotspot)
        except:
            return False
        return True

        
    def hotspot_login(self):    
        driver = webdriver.Firefox()
        driver.get(self.hotspot)
        #e = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
        e = driver.find_element(By.XPATH, '/html/body/div/form/input[3]')
        e.clear()        
        e.send_keys(self.username)
        e.send_keys(Keys.ENTER)
        time.sleep(10)
        driver.close()

if __name__=="__main__":
    website = sys.argv[1]
    hotspot = sys.argv[2]
    user = sys.argv[3]

    i = Internet(website, hotspot, user)
    site_up = i.check_website()
    hotspot_up = i.check_hotspot()
    print(f"Website {'up' if site_up else 'down'}") 
    print(f"Hotspot {'up' if hotspot_up else 'down'}")
    
    if not site_up and hotspot_up:
        with Display(visible=False, size=(800, 400)):
            i.hotspot_login()



