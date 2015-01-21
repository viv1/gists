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



