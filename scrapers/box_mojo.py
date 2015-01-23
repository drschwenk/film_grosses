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
	if not obj:
		return None
	next_sibling = obj.findNextSibling()

	if next_sibling:
		return next_sibling.text
	else:
		return None
def strip_unicode(string):
	'''Helper function to strip unicode characters from the data strings stored in the data dictionary'''
	return string.decode('unicode_escape').encode('ascii','ignore')

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
	#TODO add- genre, budget, awards, Distributor, cast (later from IMDB)
	properties = ['title',
                  'domestic_total_gross',
                  'release_date',
                  'runtime_mins',
                  'rating',
                  'budget']

	property_list = []

	def process_property(property):
		'''This function takes a property from the list of properties and
		finds the corresponding value in the bs representation of a webpage.
		The property is processed and formatted for numerical work in pandas.
		'''

		if property == 'title':
			title_string = soup.find('title').text
			title = strip_unicode(title_string.split('(')[0].strip())
			property_list.append(title)
		elif property == 'domestic_total_gross':
			raw_gross = getval(soup, 'Domestic Total')
			try:
				moneystring = int(raw_gross.replace('$', '').replace(',',''))
				property_list.append(moneystring)
			except AttributeError:
				property_list.append(None)
		elif property == 'release_date':
			raw_rel_date = getval(soup, 'Release Date')
			try:
				date = dateutil.parser.parse(raw_rel_date).date()
				property_list.append(date)
			except:
				property_list.append(None)
		elif property == 'runtime':
			raw_runtime = getval(soup, 'Runtime')
			runtime = raw_runtime.split()
			try:
				minutes = int(runtime[0])*60 + int(runtime[2])
				property_list.append(minutes)
			except:
				property_list.append(None)
		elif property == 'rating':
			try:
				rating = strip_unicode(getval(soup, 'MPAA Rating'))
				property_list.append(rating)
			except:
				property_list.append(None)
		elif property =='budget':
			raw_budget =getval(soup, 'Production Budget')
			try:
				budget = strip_unicode(raw_budget.split()[0])
				budget_in_dollars = float(budget.split('$')[1])*10**6
				property_list.append(budget_in_dollars)
			except:
				property_list.append(None)


		else:
			property_list.append(None)

	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)

	for property in properties:
		process_property(property)

	movie_dict = dict(zip(properties, property_list))

	return movie_dict

def make_complete_movie_dataset(franchise_url_list):
	'''Takes dictionary of franchise url and returns a flattened list of all
	movies in the dataset. It also adds a franchise property to the data to preserve this information
	 This prepares the data for a pandas dataframe.
	'''
	complete_data_list= []

	for franchise, urls in franchise_url_list.iteritems():
		franchise_data = make_series_data(urls)
		for movie in franchise_data:
			movie["franchise"] = franchise
			complete_data_list.append(movie)

	return complete_data_list


def makeplot_grosses(movie_list):
	'''Generates and returns line plot of the gross returns over the
	  course of a series
	'''
	indices = [i for i in range(1,len(movie_list)+1)]
	grosses = [int(movie['domestic_total_gross'])/1000000 for movie in movie_list]
	grossplot=plt.plot(indices, grosses);
	return grossplot