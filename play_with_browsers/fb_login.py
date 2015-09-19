# Simple script to login to facebook
# Supports only python2 
# just change raw_input to input and it will support python3 also.

# Requires selenium to be installed....
# sudo python2 -m pip install selenium (or sudo python3 -m pip install selenium)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.fb.com")

user=raw_input("Enter user email or phone no.")
pwd=raw_input("Enter your password")

username=driver.find_element_by_name("email")
username.send_keys(user)

password=driver.find_element_by_name("pass")
password.send_keys(pwd)

driver.find_element_by_id("loginbutton").click()

el=driver.find_element_by_class_name("_5861 textInput _586g _586p focus_target")

el.send_keys("Sahu")
el.send_keys(Keys.RETURN)


