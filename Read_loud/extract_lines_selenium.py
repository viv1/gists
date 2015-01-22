#!/usr/bin/python

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://www.huffingtonpost.com/lolly-daskal-/100-motivational-quotes-t_b_4505356.html?ir=India")

lines = driver.find_elements_by_tag_name("p")

orig_stdout=sys.stdout
f=file('quotes.txt','w')
sys.stdout=f

for i in range(5,104):
    print(lines[i].text)

sys_stdout=orig_stdout
f.close()
