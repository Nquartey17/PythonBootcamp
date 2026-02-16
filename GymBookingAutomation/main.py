import os
from selenium import webdriver

#Keep Chrome running after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

#Selenium user profile to store data
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
#Directory where data is stored
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")