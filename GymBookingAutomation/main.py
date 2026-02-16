import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Don't delete unversioned files
ACCOUNT_EMAIL = "niikwarteiq@test.com"
ACCOUNT_PASSWORD = "zmalqp12"
GYM_URL = "https://appbrewery.github.io/gym/"

#Selenium user profile to store data
#This needs to be done first or login credentials won't be saved
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

#Keep Chrome running after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#Directory where data is stored
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

#Wait for website to load
wait = WebDriverWait(driver,2)

#Wait for login button then click
login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(ACCOUNT_PASSWORD)

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click()

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
