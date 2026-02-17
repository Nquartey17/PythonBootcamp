import os
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

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

# Used admin controls to create 50% network errors
# In case of network error, creating a retry function
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)



#Wait for website to load
wait = WebDriverWait(driver,10)

def login():
    #Wait for login button then click
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear() #Clear text box in network error
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# Verify booking click goes through in case of network error
def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked" or booking_button.text == "Waitlisted")

retry(login, description="login")

#Book the next Tuesday 6pm class
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked_classes = 0
waitlists = 0
already_booked_count = 0
detailed_classes = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            class_info = f"{class_name} on {day_title}"
            if button.text == "Waitlisted":
                already_booked_count += 1
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                detailed_classes.append(f"• [Currently Waitlisted] " + class_info)
            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlisting")
                button.click()
                waitlists += 1
                print(f"✓ Joined waitlist for: {class_name}: {day_title}")
                detailed_classes.append(f"• [New Waitlist] " + class_info)
                time.sleep(0.5) #Wait for button status to update
            elif button.text == "Booked":
                already_booked_count += 1
                print(f"✓ Already booked: {class_name} on {day_title}")
                detailed_classes.append(f"• [Currently Booked] " + class_info)
            else:
                retry(lambda: book_class(button), description="Booking")
                button.click()
                booked_classes += 1
                print(f"✓ Booked: {class_name} on {day_title}")
                detailed_classes.append(f"• [New Booking] " + class_info)
                time.sleep(0.5)  # Wait for button status to update


print("--- BOOKING SUMMARY ---\n"
      f"Classes booked: {booked_classes}\n"
      f"Waitlists joined: {waitlists}\n"
      f"Already booked/waitlisted: {already_booked_count}\n"
      f"Total Tuesday & Thursday 6pm classes processed: {booked_classes + waitlists + already_booked_count}")

print("--- DETAILED CLASS LIST ---")
for status in detailed_classes:
    print(status)

