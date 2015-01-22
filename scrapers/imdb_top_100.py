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

titlelist = []
titlessoup = soup.find_all("td", "title")
for title in titlessoup:
	titlelist.append(title.text)
print titlelist

# obj = soup.find(text = re.compile(fieldname))
# next_sibling = obj.findNextSibling()

