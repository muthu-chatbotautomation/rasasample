import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
# get the path of ChromeDriverServer
chrome_driver_path = "/var/lib/jenkins/workspace/rasa pipeline/Selenium_Webdriver/chromedriver"
class Selenium_Test(unittest.TestCase):
    def test_Selenium_Unit_Test(self):
        # create a new Chrome session
        options1 = Options()
        options1.add_argument('--no-sandbox')
        options1.add_argument("--headless")
        options1.add_argument('--disable-gpu')
         # Last I checked this was necessary.

        driver = webdriver.Chrome(chrome_driver_path, options=options1)
        # driver = webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(30)
        driver.maximize_window()
        

        # chatbot testing simulation
        time.sleep(12)
        driver.get('http://sidwebpage.s3.us-east-2.amazonaws.com/website/index.html')
        print(driver.current_url)
        time.sleep(12)
        driver.refresh()
        time.sleep(12)
        driver.find_element_by_xpath('//*[@id="webchat"]/div/button ').click()
        time.sleep(12)
        Mousepointer = driver.find_element_by_class_name("new-message")
        driver.execute_script("arguments[0].click();",Mousepointer)
        print("Mousepointer value{0}".format(Mousepointer))
        Mousepointer.send_keys("Hi")
        Mousepointer.send_keys(Keys.ENTER)


if __name__ == '__main__':
    unittest.main()

