from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome running after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_num = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
#click on link with selenium
# article_num.click()

#Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

#Input text in search bar
search = driver.find_element(By.NAME, value="search")
driver.maximize_window() #Maximize screen so text can appear in search bar

search.send_keys("Python",Keys.ENTER)
