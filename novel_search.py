import requests
from bs4 import BeautifulSoup
import time

# chapters range
start, end = 1350, 1600
# link(must be in format that after adding chapter number at the end it is valid)
link = "https://novelbin.novel-online.org/novel/super-gene/chapter-"
# keyword to search
keyword = "rank"

for i in range(start, end):
	finalLink = link + str(i)
	response = requests.get(finalLink)

	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		
		matching_elements = soup.find_all(string=lambda text: keyword in str(text).lower())
		
		if matching_elements:
			print("'{}' found in the chapter {}:".format(keyword, i))
	else:
		print("Failed to retrieve chapter {}. Got status code {}. Link: {}".format(i, response.status_code, finalLink))
	time.sleep(0.1)