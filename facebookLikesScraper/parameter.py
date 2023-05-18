#Facebook Credentials
Facebook_username = 'Enter Your Email or Username'
Facebook_password = 'Password'
#url from which need to scrape data
URL= "https://www.facebook.com/groups/1225966920763001"
#Enter the relative path of your chromedriver
relative_path = "./chromedriver.exe"

# Define the Random file name
length = 5
# Generate a random string
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Get the current timestamp
timestamp = time.strftime("%Y%m%d%H%M%S")
fileName = timestamp + random_string + '.csv' #this the generated filename
print("Your output file is: ",fileName )

#Enter number of scrolls you want.
noOfScrolls = 100
