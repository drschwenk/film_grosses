__author__ = 'schwenk'

from box_mojo import strip_unicode
from collections import defaultdict
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import dateutil.parser
import pylab


# def strip_unicode(string):
# 	'''Helper function to strip unicode characters from the data strings stored in the data dictionary'''
# 	return string.decode('unicode_escape').encode('ascii','ignore')

def build_franchise_chart_urls():
	'''Parses the franchises page on boxofficemojo.com and returns
	a list of the urls pointing to the individual franchise chart pages.
	'''
	url_base = "http://boxofficemojo.com/franchises/"
	page = urllib.request.urlopen(url_base)
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
	'''Takes a list containing urls for a particular franchise chart page, parses it, and returns a
	dictionary of the form {(franchise name):[movies in that franchise]},
	where the movies franchise value is a list of urls pointing to the individual pages for that franchise
	'''
	url_base = "http://boxofficemojo.com"
	adjust_gross_url = "&adjust_yr=2015&p="+"htm"

	franchise_url_dict = defaultdict(list)
	for franchise in franchise_list:
		page = urllib.request.urlopen(franchise)
		soup = BeautifulSoup(page)
		movie_title =soup.find_all("b")
		title_list =[]
		for title in movie_title:
			parent = title.parent
			try:
				new_url = url_base + parent['href'] +adjust_gross_url
				if new_url not in title_list and parent['href']:
					title_list.append(new_url)
			except KeyError:
				pass

		title_list_ustrip = [strip_unicode(title) for title in title_list]
		key = title_list_ustrip[1].split('=')[2].split('.')[0]
		franchise_url_dict[key] = title_list_ustrip[2:]

	return franchise_url_dict

