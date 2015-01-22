#!/usr/bin/python

# Extracts 99 motivational quotes from huffingtonpost and stores into a file.

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://www.huffingtonpost.com/lolly-daskal-/100-motivational-quotes-t_b_4505356.html?ir=India")

lines = driver.find_elements_by_tag_name("p") #Find the tags containing quotes

orig_stdout=sys.stdout                      
f=file('original_quotes.txt','w')
sys.stdout=f                                    # For outputting to a file

for i in range(5,104):
    print(lines[i].text)                        # Get the quotes

sys_stdout=orig_stdout                          # Change back to original stdout
f.close()                                       # Close file
