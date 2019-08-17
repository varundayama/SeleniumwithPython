from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver object
driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Desktop\\Selenium Libs\\Selenium files\\Selenium Libs\\chromedriver_win32\\chromedriver.exe")
# no system.setproperty

driver.get("http://newtours.demoaut.com/")      #getting to the specified page

print(driver.title)     #get Title for the page
print(driver.current_url)   #get Current URL

#print(driver.page_source)   #huge HTML code for the page

signon = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")
signon.click()
time.sleep(3)
username = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[1]/td[2]/input")
username.send_keys("mercury")
time.sleep(3)
password =driver.find_element_by_xpath("//input[@name='password']")
password.send_keys("mercury")
driver.find_element_by_xpath("//input[@name='login']").click()

#--------------------------------------
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]").click()
driver.find_element_by_name("findFlights").click()

print(driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[3]/td[1]/input").is_displayed())
print("Thanks for Testing with selenium")

#---------------------------------

driver.close()  #close current focused Browser