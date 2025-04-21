from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url=URL)

cookie = driver.find_element(By.ID, "cookie")
start_time = time.time()
increment = 5

while True:
    if time.time() > increment + start_time:
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
            for item in upgrades[::-1]:
                item.click()
        except:
            print("no upgrades available")
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")
            for item in products[::-1]:
                item.click()
        except:
            print("not enough cookies")

        start_time = time.time()
        increment += 5
    cookie.click()