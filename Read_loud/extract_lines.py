#usr/bin/python

# Couldn't get the code to run perfectly usin BeautifulSoup. Extracted using selenium instead.Code snippet for selenium version in other file.

#Will come back to this later

from bs4 import BeautifulSoup
import urllib2

url=raw_input("Enter website")

data=urllib2.urlopen(url)

soup=BeautifulSoup(data.read())
soup.prettify()

lines = soup.findAll('p')

print lines
#for line in lines:
    #print line.string



