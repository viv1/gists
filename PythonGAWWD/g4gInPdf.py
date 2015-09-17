
import httplib2
import pdfcrowd
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
					page_links.append(link)


if __name__ == '__main__':

	http=httplib2.Http()

	g4g="http://www.geeksforgeeks.org"

	site="http://www.geeksforgeeks.org/tag/dynamic-programming/page/"

	page_links=[]

	total_pages=findPageCount(site)
	populateLink(total_pages)
	#print page_links
	print len(page_links)+ "Links found"




