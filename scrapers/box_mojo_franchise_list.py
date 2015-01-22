__author__ = 'schwenk'

# from box_mojo import *
from collections import defaultdict
from bs4 import BeautifulSoup
import urllib2
import re
import dateutil.parser
import pylab


def strip_unicode(string):
	'''Helper function to strip unicode characters from the data strings stored in the data dictionary'''
	return string.decode('unicode_escape').encode('ascii','ignore')

def build_franchise_chart_urls():
	url_base = "http://boxofficemojo.com/franchises/"
	page = urllib2.urlopen(url_base)
	soup = BeautifulSoup(page)
	tablelist=[]
	franchise_titles = soup.find_all("b")

	for franchise in franchise_titles:
		tablelist.append(franchise.parent)
	franchise_list = tablelist[3:-1]

	chart_urls = []
	for franchise in franchise_list:
		chart_urls.append(url_base + franchise['href'])

	return chart_urls

def build_movie_url_list(franchise_list):
	url_base = "http://boxofficemojo.com"

	franchise_url_dict = defaultdict(list)
	for franchise in franchise_list:

		page = urllib2.urlopen(franchise)
		soup = BeautifulSoup(page)
		movie_title =soup.find_all("b")
		title_list =[]
		for title in movie_title:
			parent = title.parent
			try:
				new_url = url_base + parent['href']
				if new_url not in title_list:
					title_list.append(new_url)
			except KeyError:
				pass

		title_list_ustrip = [strip_unicode(title) for title in title_list]
		key = title_list_ustrip[1].split('=')[2].split('.')[0]
		franchise_url_dict[key] = title_list_ustrip[2:]

	return franchise_url_dict

def test_function():
	print "itworked"

# franchiseslist = build_franchise_chart_urls()
# movie_urls = build_movie_url_list(franchiseslist)
