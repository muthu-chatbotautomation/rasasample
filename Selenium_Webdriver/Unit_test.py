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

__author__ = 'Hanon'
class Selenium_Test(unittest.TestCase):
    def test_Selenium_Unit_Test(self):
        chrome_driver_path = "/var/lib/jenkins/workspace/rasa pipeline/Selenium_Webdriver/chromedriver"
        # create a new Chrome session
        # from pyvirtualdisplay import Display
        # display = Display(visible=0, size=(800, 600))
        # display.start()
#         options = webdriver.FirefoxOptions()
#         options.add_argument('-headless')
                 # Last I checked this was necessary.

        #         driver = webdriver.Chrome(chrome_driver_path, options=options1)
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.common.keys import Keys

        options1 = Options()
        options1.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'/geckodriver.exe',options=options1)
        driver.implicitly_wait(30)
        time.sleep(12)   
        driver.get('http://sidwebpage.s3.us-east-2.amazonaws.com/website/index.html')
        print(driver.current_url)        
        time.sleep(5)
        driver.refresh()   
        time.sleep(5)
        # chatbot testing simulation
        driver.find_element_by_xpath('//*[@id="webchat"]/div/button ').click()
        time.sleep(5)
        Mousepointer = driver.find_element_by_xpath('//*[@id="webchat"]/div/div/form/input')
        Mousepointer.send_keys("Hi")
        Mousepointer.send_keys(Keys.ENTER)
        ExpectedReply = "Hey! How are you Muthu?"
        Reply = driver.find_element_by_xpath('//*[@id="messages"]/div[2]/div/div/div/p/span').text
        print(Reply)
        self.assertEqual(Reply, ExpectedReply)
        print("Success")
        driver.quit()


if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
       
        
        
        
        
       
        





