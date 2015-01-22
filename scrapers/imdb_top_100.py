__author__ = 'schwenk'
from box_mojo import *

url = "http://www.imdb.com/list/ls006722960/?start=1&view=compact&sort=listorian:asc"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

# table = soup.find("table")
# print table

# for link in soup.find_all('a'):
#     print(link.get('href'))

# <td class="title"><a href="/title/tt0133093/">The Matrix</a></td>

def process_titles(string):
	'''Helper function to strip unicode characters from the data strings stored in the data dictionary'''
	title_word_list = string.split()
	if title_word_list[0] == u'The':
		del(title_word_list[0])
	title = ''
	for word in title_word_list:
		title += word
	return title


titlelist = []
titlessoup = soup.find_all("td", "title")
for title in titlessoup:
	titlelist.append(process_titles(title.text))

for title in titlelist:
	print title



# obj = soup.find(text = re.compile(fieldname))
# next_sibling = obj.findNextSibling()

# t1 =  u'The Matrix Revolutions'
#
# print process_titles(t1)