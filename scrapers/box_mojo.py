import urllib2
from bs4 import BeautifulSoup
import re
import dateutil.parser
import pylab
import matplotlib.pyplot as plt




def getval(soup, fieldname):
	'''Function finds and returns next sibling of the string given in fieldname
	'''
	obj = soup.find(text = re.compile(fieldname))
	if not obj: return None
	next_sibling = obj.findNextSibling()

	if next_sibling: return next_sibling.text
	else: return None

def make_series_data(url_list):
	'''This Function takes a list of movie urls and calls the make movie_data function on each movie.
	It returns a list of movie data dictionaries for a particular film series.
	'''
	movie_data=[]
	for url in url_list:
		movie_data.append(make_movie_data(url))
	return movie_data

def make_movie_data(url):
	'''This function takes a url pointing to the movie's page on boxofficemojo and
	returns a dictionary containing the following properties:
	'title','domestic_total_gross','release_date','runtime_mins','rating']
	'''
	def to_date(datestring):
		'''Helper function to parse and return date object for the movies release date'''
		date = dateutil.parser.parse(datestring).date()
		return date

	def money_to_int(moneystring):
		'''Helper function to parse and return the gross domestic return on the movie '''
		moneystring = int(moneystring.replace('$', '').replace(',',''))
		return moneystring

	def runtime_to_minutes(runtimestring):
		'''Helper function to parse and return the runtime of a movie'''
		runtime = runtimestring.split()
		try:
			minutes = int(runtime[0])*60 + int(runtime[2])
			return str(minutes)
		except: return None

	def strip_unicode(string):
		'''Helper function to strip unicode characters from the data strings stored in the data dictionary'''
		return string.decode('unicode_escape').encode('ascii','ignore')

	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)

	title_string = soup.find('title').text
	title = strip_unicode(title_string.split('(')[0].strip())

	raw_rel_date = getval(soup, 'Release Date')
	rel_date = to_date(raw_rel_date)

	raw_runtime = getval(soup, "Runtime")
	runtime = runtime_to_minutes(raw_runtime)

	raw_gross = getval(soup, 'Domestic Total')
	gross = money_to_int(raw_gross)

	rating = strip_unicode(getval(soup, 'MPAA Rating'))

	headers = ['title',
           'domestic_total_gross',
           'release_date',
           'runtime_mins',
           'rating']

	movie_data = []
	movie_dict = dict(zip(headers, [title,
	                           gross,
	                           rel_date,
	                           runtime,
	                           rating]))

	movie_data.append(movie_dict)
	return movie_dict

def makeplot_grosses(movie_list):
	'''Generates and returns line plot of the gross returns over the
	  course of a series
	'''
	indices = [i for i in range(1,len(movie_list)+1)]
	grosses = [int(movie['domestic_total_gross'])/1000000 for movie in movie_list]
	grossplot=plt.plot(indices, grosses);
	return grossplot
