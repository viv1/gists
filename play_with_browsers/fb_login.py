# Simple script to login to facebook

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

