# 5 minute game, every 5 seconds buy the most expensive upgrade/product
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

#Keep Chrome running after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

#Timer added, website needs time to load before starting
sleep(1.5)
language_button = driver.find_element(by=By.ID, value="langSelect-EN")
language_button.click()

#Another loading timer added just in case
sleep(2)

#Accept cookies
accept_cookies = driver.find_element(By.CLASS_NAME, value="cc_btn_accept_all")
accept_cookies.click()

#Close multiple notifications if button appears
def close_notifications():
    try:
        notification_button = driver.find_element(By.CSS_SELECTOR, value=".framed.close.sidenote")
        notification_button.click()
    except NoSuchElementException:
        print("Notification button didn't appear")

cookie = driver.find_element(by=By.ID, value="bigCookie")
cookie.click()

# Repeat this code for 5 minutes, 5 seconds per cycle, 60 cycles total
current_cycles = 0
end_cycles = 60

while current_cycles < end_cycles:

    close_notifications()
    #keep clicking for 5 seconds
    stopwatch = time()
    while (time() - stopwatch) < 5:
        cookie.click()
    #find the most expensive product
    product_prices = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled .price")

    #find product ID by number
    price_values = []
    for product in product_prices:
        price_values.append(int(product.text))

    print(price_values)
    highest_value = max(price_values)
    highest_index = price_values.index(highest_value)
    print(f"Highest index: {highest_index}")

    #Click the product with the highest price
    #Find element by link text
    click_highest_price = driver.find_element(By.ID, value=f'product{highest_index}')
    click_highest_price.click()

    current_cycles += 1
    print(f"Current cycles: {current_cycles}")