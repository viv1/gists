#!usr/bin/python

# Script to open a site using webproxy(hidebux.com)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site=raw_input("Enter site: ")

driver = webdriver.Firefox()
driver.get("http://www.hidebux.com")

elem = driver.find_element_by_name("u")

if "http" not in site:
    site="http://"+site
    
elem.send_keys(site)
elem.send_keys(Keys.RETURN)
