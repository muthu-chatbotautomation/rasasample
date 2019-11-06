import os
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = "/var/lib/jenkins/workspace/rasa pipeline/Selenium_Webdriver"
chrome_driver_path = dir + "/chromedriver"

# create a new Chrome session
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.

driver = webdriver.Chrome(chrome_driver_path,options=options)
# driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.google.com/")
print(driver.current_url)

