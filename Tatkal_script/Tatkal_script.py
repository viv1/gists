#!/usr/bin/python

#This script will book Tatkal tickets for you
#You will have to provide a few details before_hand

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.irctc.co.in/eticketing/loginHome.jsf")
driver.save_screenshot('irctc.png')
driver.find_element_by_class_name("loginUserId").send_keys("bhuwanlals")
driver.find_element_by_class_name("loginPassword").send_keys("bep149")


driver.quit()

"""

TO DO

1.Use find element to find login and pwd boxes and fill it up.
2.Use pytesseract to extract text from captcha

"""
