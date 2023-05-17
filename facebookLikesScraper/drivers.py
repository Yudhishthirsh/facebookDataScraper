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
import pandas as pd
import parameter

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(parameter.relative_path, chrome_options=chrome_options)