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

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
from selenium.webdriver.support.wait import WebDriverWait
# s = Service('/Users/username/bin/chromedriver.exe')
# driver = webdriver.Chrome(service=s, options=chrome_options)
driver = webdriver.Chrome('/Users/username/bin/chromedriver', chrome_options=chrome_options)
from ..items import QuotesItem
class QuotesSpider(scrapy.Spider):
    name = "test"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
    allowed_domains = ["facebook.com"]
    handle_httpstatus_list = [999]  # without this line the crawler would stop

    # working since it ignores all the non 200 responses
    def start_requests(self):
        print("start time is ")
        print(time.time())

        # content_list = []
        # name_list = []
        # comment_name_list = []
        # comment = []
        # like_person = []
        # total_like = []
        # open the webpage
        driver.get("https://wwww.facebook.com/")
        # target username
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        print(username)
        # enter username and password
        username.clear()
        username.send_keys("priyanshusahu153@gmail.com")
        password.clear()
        # use your username and password
        password.send_keys("IIItg@123")
        # target the login button and click it
        time.sleep(2)
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        # We are logged in!
        print("Logged in")
        # program to parse user name who posted comment
        time.sleep(2)
        # driver.quit()
        url1="https://www.facebook.com/groups/1225966920763001"
        yield scrapy.Request(url1, callback=self.parse)

        print("end time is ")
        print(time.time())

    def parse(self, response):
        # print('url is: ', response.url)
        # driver.get('https://uk.linkedin.com/in/pauljgarner')
        items = QuotesItem()
        driver.get(response.url)
        actions = ActionChains(driver)
        time.sleep(2)
        content_list = []
        name_list = []
        comment_name_list = []
        comment = []
        like_person = []
        total_like = []
        all_posts = []
        soup = BeautifulSoup(driver.page_source, "html.parser")
        s1 = driver.page_source
        df = pd.DataFrame()
        for i in range(1, 100):
            new_posts = []
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            posts = driver.find_elements(By.XPATH, "//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
            # print("---------------------------------------")
            print("Length of all posts found in current iteration:", len(posts))
            # print("---------------------------------------")
            # print(len(posts))
            isPostLiked = True
            for post in posts:
                if post not in all_posts:
                    try:
                        name = post.find_element('xpath',
                                                 ".//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f']").text
                        print("---------------------------------------")
                        print("Person who posted:", name)
                        # print("---------------------------------------")
                    except:
                        print("name not found")
                    try:
                        content = post.find_element('xpath',
                                                    ".//div[@class='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a']").text
                        #    content=post.find("div",{"class":"x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a"}).text
                    except:
                        content = "not found"
                    print("content of the post:", content)
                    try:
                        likeButton = post.find_element('xpath', ".//span[@class='x1e558r4']")
                        numberOfLikes = likeButton.text
                        # print("---------------------------------------")
                        print("Number of likes for this post:", numberOfLikes)
                        # print("---------------------------------------")
                        isPostLiked = True
                    except:
                        isPostLiked = False
                    if (isPostLiked == True):
                        try:
                            if ((likeButton.is_displayed()) and (likeButton.is_enabled())):
                                driver.execute_script("arguments[0].click();", likeButton)
                                time.sleep(1)
                                print("Like PopUp Window Open")
                                liker_list = set()
                                while (len(liker_list) < int(numberOfLikes)):
                                    element_inside_popup = post.find_element(By.XPATH, "//div[@class=' x1rg5ohu']//a")
                                    time.sleep(2)
                                    element_inside_popup.send_keys(Keys.END)
                                    time.sleep(2)

                                    person_like = driver.find_elements(By.XPATH, ".//div[@class=' x1rg5ohu']")
                                    time.sleep(2)
                                    # print("---------------------------------------")
                                    print("People who liked this post:")
                                    # print("---------------------------------------")
                                    for f in person_like:
                                        print(f.text)
                                        liker_list.add(f.text)
                                        time.sleep(1)
                                close = driver.find_element('xpath',
                                                            "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1']")
                                close.click()
                                time.sleep(1)
                                print("Pop Window is Closed")
                                print(liker_list)
                        except Exception as e:
                            print(e)
                all_posts.append(post)
                print("---------------------------------------------")
            # content_list.append(content)
                items['postername']=name
                items['totallike']=numberOfLikes
                items['likepeople']=liker_list
                items['Post_content']=content
                yield items
            # name_list.append(name)
            # comment_name_list.append(comname)
            # comment.append(com)
            # # time_list.append(timing)
            # like_person.append(liker_list)
            # total_like.append(numberOfLikes)
            # df=pd.DataFrame({"postername":name_list,"Total_Likes(Per Post)":total_like,"Like_People":like_person})
            # # # df.drop_duplicates(subset="content",keep="first",inplace=True)
            # df.to_csv("fb_data3.4.11.csv")