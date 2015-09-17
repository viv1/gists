#Script to convert HTML pages of geeksforgeeks into pdf and save it in your Downloads directory.
#Identifies pages to be converted based on tags
#Uses pdfkit to convert html to pdf and httplib2 and BeautifulSoup to get requested page and parsing
import httplib2
import pdfcrowd
import pdfkit
import os
from bs4 import BeautifulSoup, SoupStrainer


#finds number of pages with given tag
def findPageCount(link):
	curr_page_tag=[]
	page_count=0
	while len(curr_page_tag) < 1:
		page_count = page_count+1
		(status, content) = http.request(site+str(page_count))
		curr_page_tag=BeautifulSoup(content, parse_only=SoupStrainer(content="Page Not Found - GeeksforGeeks"))
	return (page_count-1)
	
#Populates based on asked for Tag 
def populateLink(last_page):
	for page_num in range(1, last_page+1):
		(status, content) = http.request(site+str(page_num))

		soup = BeautifulSoup(content)
		div_content = soup.find("section", {"class": "site-content"})
		
		div_tags=div_content.find_all("a")

		for elem in div_tags:
			if elem.has_attr('href'):
				link=elem['href']
				if link.find(g4g)==0 and link.find('category') < 0 and link.find('tag')<0 and link.find('#')<0:
					if(link.find('u')==0):
						link=str(link)
					page_links.append(link)

#html to pdf conversion
def convertToPDF(page_links, type):
	link_count=1
	for i in page_links:
		file_loc="/home/vivek/Downloads/GeeksforGeeks/"+type+"/"
		file_name=type+str(link_count)+".pdf"
		try:
			pdfkit.from_url(str(i), file_loc+file_name)
		except:
			print("Some conversion error in "+ str(i))
		link_count=link_count+1



if __name__ == '__main__':

	http=httplib2.Http()

	g4g="http://www.geeksforgeeks.org"

	dict=["dynamic-programming","advance-data-structures", "Greedy-Algorithm", "backtracking", "pattern-searching", "divide-and-conquer", "MathematicalAlgo", "recursion", "geometric-algorithms", "other"]

	tag_num=0
	for li in dict:
		tag_num=tag_num+1
		print str(tag_num)+"-->"+ li

	whichTag=input("Input tag number: ")


	site="http://www.geeksforgeeks.org/tag/"+dict[whichTag-1]+"/page/"
	page_links=[]

	try:
		dir_loc="/home/vivek/Downloads/GeeksforGeeks/"+dict[whichTag-1]
		os.makedirs(dir_loc)
	except:
		pass

	total_pages=findPageCount(site)

	populateLink(total_pages)
	print page_links
	print str(len(page_links))+ " Links found"

	convertToPDF(page_links, dict[whichTag-1])

	print "Conversion completed Successfully"




