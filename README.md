# facebookDataScraper

Download pycharm and setup virtual enviroment in your pycharm inside the folder facebookDataScraper using Command in terminal below.

pip install virtualenv or can follow the below link to create virtual Environment

https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements

After creating virtual environment in your project. install scrapy package in pycharm , install instaloader package using pip install instaloader , install pandas into the terminal using pip install pandas command in the Terminal To install all these packages use command: 

pip install -r requirements.text

Before Running the spider run this command to create python path for all python files in the directory

$env:PYTHONPATH = "Path of Directory;$env:PYTHONPATH" 

Path of Directory:Main Project Directory which includes all files such as login,requirement and parameter, login, drivers.

Now,
To scrape data from facebook public groups you need a facebook login. Need to add your credentials in parameter.py file.

1)Facebook_username = 'Enter Your Email or Username'

2)Facebook_password = 'Password'

#url from which need to scrape data

3)URL= "https://www.facebook.com/groups/1225966920763001" #(sample URL)

#Enter the relative path of your chromedriver

4)relative_path = "./chromedriver.exe"

#Enter number of scrolls you want.

5)noOfScrolls = 100 

 Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below cd .\scraperSkeleton\

After reaching to the scraperSkeleton directory Run following command in terminal. scrapy crawl fbCrawler --nolog in the terminal. Where output.csv(for reference) is the file name in which the output will be recorded

Notes:
1) Scripts run successfully in the scrapy framework using selenium to log in to facebook and scrape data from a facebook group and can extract upto 200 times scroll through the group and retrieve ~400 posts and beyond this stage, the script encountered elements which were not available for interact
