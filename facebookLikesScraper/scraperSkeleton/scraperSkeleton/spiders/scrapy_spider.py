import scrapy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import drivers
import login
import parameter
from ..items import QuotesItem
import pandas as pd


class QuotesSpider(scrapy.Spider):
    # Enter your Scrapy Spider name
    name = "fbCrawler"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
# Enter the web domain which have to scrape
    allowed_domains = ["facebook.com"]
    # handle_httpstatus_list = [999]  # without this line the crawler would stop

#This function will call the login function and then parse function
    def start_requests(self):
        #login() function calling
        login.login()
        time.sleep(2)
        #url1 is the url of the group from which the data will be scraped
        url1 = parameter.URL
        # parse function calling
        yield scrapy.Request(url1, callback=self.parse)

#data parsing function which will be scraped from the website.
    def parse(self, response, **kwargs):
        data = []
        global posterName, peopleLiked, postContent, numberOfLikes
        items = QuotesItem()
        drivers.driver.get(response.url)
        time.sleep(2)
        all_posts = []
        for i in range(1, parameter.noOfScrolls):
            new_posts = []
            time.sleep(2)
            drivers.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            posts = drivers.driver.find_elements(By.XPATH, "//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
            time.sleep(1)
            for post in posts:
                if post not in all_posts:
                    try:
                        posterName = post.find_element('xpath',
                                                 ".//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f']").text
                        #in posterName variable we are getting name of the person who posted
                        print("Person who posted:", posterName)
                    except:
                        print("name not found") # if the posterName is not found then 
                    try:
                        postContent = post.find_element('xpath',
                                                    ".//div[@class='x1iorvi4 x1pi30zi x1swvt13 xjkvuk6']").text
                    except:
                        postContent = "not found"
                    print("content of the post:", postContent)# if the postContent is not found then
                    try:
                        likeButton = post.find_element('xpath', ".//span[@class='x1e558r4']")
                        time.sleep(2)
                        numberOfLikes = likeButton.text # Total number of likes will be stored in numberOfLikes
                        print("Number of likes for this post:", numberOfLikes)
                        isPostLiked = True # Like button checkpoint weather it is found on post or not
                    except:
                        isPostLiked = False
                    if (isPostLiked == True):
                        try:
                            if ((likeButton.is_displayed()) and (likeButton.is_enabled())):
                                time.sleep(2)
                                drivers.driver.execute_script("arguments[0].click();", likeButton)
                                time.sleep(3)
                                print("Like PopUp Window Open")
                                peopleLiked = set()
                                while (len(peopleLiked) < int(numberOfLikes)):
                                    time.sleep(3)
                                    element_inside_popup = post.find_element(By.XPATH, "//div[@class='x1rg5ohu']//a")
                                    time.sleep(2)
                                    element_inside_popup.send_keys(Keys.END)
                                    time.sleep(2)

                                    personLiked = drivers.driver.find_elements(By.XPATH, ".//div[@class='x1rg5ohu']")
                                    time.sleep(2)
                                    print("People who liked this post:")
                                    for personName in personLiked:
                                        print(personName.text)
                                        peopleLiked.add(personName.text)
                                        time.sleep(0.5)
                                time.sleep(2)
                                close = drivers.driver.find_element('xpath',
                                                                    "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1']")
                                close.click()
                                time.sleep(3)
                                print("Pop Window is Closed")
                                print(peopleLiked)
                        except Exception as e:
                            print(e)
                all_posts.append(post)
                # content_list.append(content)
                parsedData = {
                'posterName' : posterName,
                'numberOfLikes' : numberOfLikes,
                'peopleLiked' : peopleLiked,
                'postContent' : postContent
                }
                data.append(parsedData)
                df = pd.DataFrame(data)
                df.to_csv('output.csv', index=False)
                yield items
