import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException
from datetime import date, datetime, timedelta

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
wait = WebDriverWait(driver,10)

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

#Book the next Tuesday 6pm class day-group-today/-tomorrow/-tue
#Idea: if today is tuesday: today. if tomorrow: -tomorrow, else: -tue
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button.click()

            print(f"✓ Booked: {class_name} on {day_title}")
