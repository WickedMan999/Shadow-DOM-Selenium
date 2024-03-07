from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variables
base_url = "https://selectorshub.com/xpath-practice-page/"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Actionchains Instance
action = ActionChains(driver)

# Open URL
driver.get(base_url)
time.sleep(3)

# Locating nearby element of DOM 1
main_dom = driver.find_element(
    By.CSS_SELECTOR, "#userName").shadow_root

# Locate 'username' text field element inside of Dom 1 and click
username = main_dom.find_element(By.CSS_SELECTOR, "#kils")
username.click()

# Navigating to closed shadow dom using actionchains [tab 3 times]
for i in range(3):
    action.send_keys(Keys.TAB).perform()
    time.sleep(1)

# Finally, enter password on 'Concept Test' element once it reaches there
action.send_keys(
    "No, DevTools CTRL+F doesn't always give right count of XPATH match").perform()

time.sleep(5)
