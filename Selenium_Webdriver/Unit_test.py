import os
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

# get the path of ChromeDriverServer

chrome_driver_path = "/var/lib/jenkins/workspace/rasa pipeline/Selenium_Webdriver/chromedriver"

class Selenium_Test(unittest.TestCase):
    def test_Selenium_Unit_Test(self):
        # create a new Chrome session
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(chrome_driver_path, options=options)
        # driver = webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(30)
        driver.maximize_window()
        # chatbot testing simulation
        time.sleep(12)
        driver.get('http://sidwebpage.s3.us-east-2.amazonaws.com/website/index.html')
        print(driver.current_url)
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="webchat"]/div/button').click()
        Mousepointer = driver.find_element_by_xpath('//*[@id="webchat"]/div/div/form/input')
        print("Mousepointer value{0}".format(Mousepointer))
        Mousepointer.click()
        Mousepointer.send_keys("Hi")
        time.sleep(2)
        Mousepointer = driver.find_element_by_xpath('//*[@id="webchat"]/div/div/form/button/img')
        Mousepointer.click()
        time.sleep(3)
         # displaying and validating value
        ExpectedReply = "Hey! How are you Easwar?"
        Reply = driver.find_element_by_xpath('//*[@id="messages"]/div[2]/div/div/div/p/span').text
        print(Reply)
        self.assertEqual(Reply, ExpectedReply)
        print("Success")
if __name__ == '__main__':
    unittest.main()


