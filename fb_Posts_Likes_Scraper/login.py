import scrapy
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import parameter
import drivers
def login():
        drivers.driver.get("https://wwww.facebook.com/")
        # target username
        username = WebDriverWait(drivers.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(drivers.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        print(username)
        # enter username and password
        username.clear()
        username.send_keys(parameter.Facebook_username)
        password.clear()
        # use your username and password
        password.send_keys(parameter.Facebook_password)
        # target the login button and click it
        time.sleep(2)
        button = WebDriverWait(drivers.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        # We are logged in!
        print("Logged in")
        # program to parse user name who posted comment