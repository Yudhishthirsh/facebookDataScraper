# facebookDataScraper
This is the Facebook Scraping Framework which can be able to scrape publicly available data that is available on particular facebook page.
--
Using this script following data can be scraped from the facebook public pages:

--"posterName" - Person name who has posted on the facebook page

--"numberOfLikes" - Number of likes on a same post

--"peopleLiked" - People name who have liked the post

--"postContent" - Content written in post

This script supports linux, windows OS.

The script description is mentioned below
--

1) Open the project and go to the facebookLikesScraper in your windows terminal or on linux operating system.

2) Install all the required python packages using below command: 

         pip install -r requirements.txt

3) Now go to the project directory using command below:

         cd .\facebookLikesScraper\

4) After reaching LinkedlnProfileUrlScraper directory run below command to create the Python path over all the directories and files in the project.

a) Command for Windows OS:

               command = $env:PYTHONPATH = "Absolute Path of Directory;$env:PYTHONPATH" # Abslolute path of this "facebookLikesScraper" directory
  
While entering Absolute path of the directory ensure to change backword Slash (/) into forward slash(\) inside the path in case when running in windows machine.
              
To run this script in cmd.exe in windows os :

              set PYTHONPATH=Absolute path of the directory;%PYTHONPATH%
             
              No need of changing backward slashes in (/) while using cmd.exe

b) Command for linux OS:   

               Command : export PYTHONPATH="Absolute Path of Directory" # Abslolute path of this "facebookLikesScraper" directory i your linux machine
  
               In this case there is no need to change backward slash.

Now, to scrape data from facebook public groups you need a facebook login. Need to add your credentials in parameter.py file.

   a) Facebook_username = 'Enter Your Email or Username'

   b) Facebook_password = 'Password'

   c) url from which need to scrape data
   
      URL= "https://www.facebook.com/groups/1225966920763001" #(sample URL)

   d) Enter the relative path of your chromedriver (Ensure that there is chrome browser application installed in your machine)
    
          For Windows OS : chromeDriverPath = "./chromedriver.exe"
    
          For linux Machinne: chromeDriverPath = "./chromedriver" #In case when running this script in linux machine then need to update the chromeDriverPath.
          
          Need to save the latest chromedriver versions for both linux and windows OS in order to run script successfully.

   e) Enter number of scrolls you want.
            noOfScrolls = 100 


6)Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below 

         Command : cd .\scraperSkeleton\

7) After reaching to the scraperSkeleton directory Run following command in terminal. 

         Command : scrapy crawl fbCrawler --nolog 

8) The outputfile of the scraped records is generated inside scraperSkeleton(outer) folder having random name which has nomenclature as given below.

     Output File name exaample : 20230518142546cfzl3.csv, 

     a) Where 20230518 is the date on which file is created

     b) Where 142546 followed by date is the time at which the file is created.
 
     c) After time there are 5 alphanumeric characters


Notes:
1) Scripts run successfully in the scrapy framework using selenium to log in to facebook and scrape data from a facebook group and can extract upto 200 times scroll through 

the group and retrieve ~400 posts and beyond this stage, the script encountered elements which were not available for interact

3) Facebook Use to change their tags and Xpath frequently, in order to overcome that element not found error need to update the Xpath and the tags. Otherwise this script will not be locate the elements on web page and hence it will not able to scrape the data.
