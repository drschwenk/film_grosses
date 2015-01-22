__author__ = 'schwenk'

from box_mojo import *



def build_franchise_chart_urls():
	url_base = "http://boxofficemojo.com/franchises/"
	page = urllib2.urlopen(url_base)
	soup = BeautifulSoup(page)
	tablelist=[]
	table = soup.find_all("b")

	for item in table:
		tablelist.append(item.parent)
	franchise_list = tablelist[3:-1]

	chart_urls = []
	for franchise in franchise_list:
		chart_urls.append(url_base + franchise['href'])

	return chart_urls



franchises = build_franchise_chart_urls()

print franchises