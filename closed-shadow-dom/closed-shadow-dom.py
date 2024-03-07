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

# Actionchains Instance
action = ActionChains(driver)

# Open URL
driver.get(base_url)
time.sleep(3)

# Scroll verically using JavaScript by offset
driver.execute_script("window.scrollBy(0, 1600);")
time.sleep(1)

# Wait 10 sec until the nearby element above closed shadow dom is presence
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='userPass']")))

# Locating nearby element of closed shadow DOM after its presence and click
nearby_element = driver.find_element(By.XPATH, "//div[@id='userPass']")
nearby_element.click()

# To interact with closed shadow dom element i.e. password i used actionchains to hit TAB to navigate on that element after clicked
action.send_keys(Keys.TAB).perform()
time.sleep(1)

# Once reached on that element, i enterd the value
action.send_keys("Password@123").perform()

time.sleep(10)
