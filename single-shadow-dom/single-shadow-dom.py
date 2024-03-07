from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Variable
base_url = "https://books-pwakit.appspot.com/"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Explicit Wait Timer
wait = WebDriverWait(driver, 10)

# Open URL
driver.get(base_url)
driver.implicitly_wait(30)

# Wait 10 sec for nearby 'Dom' element to be present
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "book-app[apptitle='BOOKS']")))

# Locating nearby DOM element once it is present
domElement = driver.find_element(
    By.CSS_SELECTOR, "book-app[apptitle='BOOKS']").shadow_root

# Find the text box element that is inside of DOM
input_element = domElement.find_element(By.CSS_SELECTOR, "#input")

# Enter the value inside text box and hit enter
input_element.send_keys("harry potter", Keys.RETURN)

# Get the value of the input field and print entered value
entered_book = input_element.get_attribute('value')
print('Book name is:', entered_book)

time.sleep(3)
