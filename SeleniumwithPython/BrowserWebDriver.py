from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # driver object
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DELL/Desktop/Selenium Libs/Selenium files/Selenium Libs/chromedriver_win32/chromedriver.exe")
        # no system.setproperty
        cls.driver.maximize_window()
        cls.driver.get("http://newtours.demoaut.com/")  # getting to the specified page

    def login_test(self):
        print(self.driver.title)  # get Title for the page
        print(self.driver.current_url)  # get Current URL
        # print(driver.page_source)   #huge HTML code for the page
        signon = self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")
        signon.click()
        time.sleep(3)
        username = self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[1]/td[2]/input")
        username.send_keys("test1")
        time.sleep(3)
        password = self.driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("123456")
        self.driver.find_element_by_xpath("//input[@name='login']").click()

    @classmethod
    def tearDownClass(cls):
        #close current focused Browser
        cls.driver.close()