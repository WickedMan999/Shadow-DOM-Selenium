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
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Open URL
driver.get(base_url)
time.sleep(5)

# Locating nearby element of DOM 1
main_dom = driver.find_element(
    By.CSS_SELECTOR, "#userName").shadow_root

# Locate 'username' text field element inside of Dom 1 & enter value
username = main_dom.find_element(By.CSS_SELECTOR, "#kils")
username.send_keys('Wicked Man')

# Get the value of the input field and print entered value
entered_username = username.get_attribute('value')
print('Entered username is:', entered_username)

# Locating nearby element of DOM 2
nested_dom = main_dom.find_element(
    By.CSS_SELECTOR, "#app2").shadow_root

# Locate 'Pizza name' text field element inside of Dom 2 & enter value
pizza_name = nested_dom.find_element(By.CSS_SELECTOR, "#pizza")
pizza_name.send_keys('Cheese Pizza')

# Get the value of the input field and print entered value
entered_username = pizza_name.get_attribute('value')
print('Pizza name is:', entered_username)

time.sleep(5)
