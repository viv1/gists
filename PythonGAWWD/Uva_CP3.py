""" 
Script to download Competitive Programming 3 questions as pdf into the system, based on category
Uses httplib2 and BeautifulSoup to get requested page and parsing
**********
Current status:
1.Program does not terminate.Look into how the list is populated. Probably repeated values.
2.Program does not go further than one depth.Likely because of 1.
3.Have to add functions to create appropriate directories and download there as pdf.


**********

@author:Vivek Sahu
"""
"""
Running instructions
>>>python Uva_CP3.py
"""
import httplib2
import os
import sys
from bs4 import BeautifulSoup

#Should populate all problem links and also find category names and links 
def populateList(prob_site):
	(status, content) = http.request(prob_site)
	to_crawl.pop()
	crawled.append(prob_site)
	soup = BeautifulSoup(content)
	div_content=soup.find("div",{"id":"col3"})
	div_c=str(div_content)
	soup = BeautifulSoup(div_c)
	table_content=soup.find("table",{"cellspacing":"0"})
	page_links=table_content.find_all("a")

	row_no=0
	for link in page_links:
		row_no=row_no+1
		if link.has_attr("href"):
			print str(row_no)+"-->"+link.get_text()
			curr_link=link["href"]
			if curr_link.find("page_show_problem")<0 and curr_link not in crawled:
				to_crawl.append(curr_link)
			if curr_link.find("page_show_problem")>-1:
				problem_links.append(curr_link)





if __name__ == '__main__':

	http=httplib2.Http()

	uva="https://uva.onlinejudge.org/"
	problem_site="index.php?option=com_onlinejudge&Itemid=8&category=675"

	to_crawl=[]
	crawled=[]
	problem_links=[]

	to_crawl.append(problem_site)
	while len(to_crawl):
		populateList(uva+str(to_crawl[0]))
	






