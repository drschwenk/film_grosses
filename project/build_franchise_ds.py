__author__ = 'schwenk'

from collections import defaultdict
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse


def build_franchise_chart_urls():
	'''Parses the franchises page on boxofficemojo.com and returns
	a list of the urls pointing to the individual franchise chart pages.
	'''
	url_base = "http://boxofficemojo.com/franchises/"
	page = urllib.request.urlopen(url_base)
	soup = BeautifulSoup(page)
	chart_titles = []
	franchise_titles = soup.find_all("b")

	for franchise in franchise_titles:
		chart_titles.append(franchise.parent)
	franchise_list = chart_titles[3:-1]

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
	adjust_gross_url = "&adjust_yr=2015&p=" + "htm"

	franchise_url_dict = defaultdict(list)
	for franchise in franchise_list:
		page = urllib.request.urlopen(franchise)
		soup = BeautifulSoup(page)
		movie_title = soup.find_all("b")
		title_list = []
		for title in movie_title:
			parent = title.parent
			try:
				new_url = url_base + parent['href'] + adjust_gross_url
				if new_url not in title_list and parent['href']:
					title_list.append(new_url)
			except KeyError:
				pass

		title_list_ustrip = [strip_unicode(title) for title in title_list]
		key = title_list_ustrip[1].split('=')[2].split('.')[0]
		franchise_url_dict[key] = title_list_ustrip[2:]

	return franchise_url_dict


def process_franchise_data(movies_df):
	franchises_dict_list = []
	for franchise, movies_df in franchise_groups:
		movies_df.drop_duplicates('title', inplace=True)
		if franchise == 'lordoftherings':
			movies_df = movies_df[movies_df.rating != 'PG']
		franchise_dict = {}
		try:
			franchise_dict['first_title'] = movies_df['title'].iloc[0]
			franchise_dict['new_title'] = movies_df['title'].iloc[2]
			franchise_dict['franchise'] = franchise
			franchise_dict['prev_gross'] = (movies_df['domestic_total_gross'].iloc[0] +
			                                movies_df['domestic_total_gross'].iloc[1]) / float(2)
			franchise_dict['act_gross'] = movies_df['domestic_total_gross'].iloc[2]
			franchise_dict['prev_meta'] = (movies_df['metacritic'].iloc[0] + movies_df['metacritic'].iloc[1]) / float(2)
			franchise_dict['act_meta'] = movies_df['metacritic'].iloc[2]
			time_d = np.timedelta64(movies_df['release_date'].iloc[1] - movies_df['release_date'].iloc[0])
			franchise_dict['days_elapsed'] = time_d.item().total_seconds() / 86400
			franchise_dict['genre'] = movies_df['genre'].iloc[2]
			franchise_dict['rating'] = movies_df['rating'].iloc[2]
			franchise_dict['director'] = movies_df['director'].iloc[2]

			if (movies_df['genre'].iloc[0] == movies_df['genre'].iloc[1] == movies_df['genre'].iloc[2]):
				franchise_dict['same_genre'] = 0.0
			else:
				franchise_dict['same_genre'] = 1.0
			if (movies_df['director'].iloc[0] == movies_df['director'].iloc[1] == movies_df['director'].iloc[2]):
				franchise_dict['same_dir'] = 0.0
			else:
				franchise_dict['same_dir'] = 1.0
			if (movies_df['rating'].iloc[0] == movies_df['rating'].iloc[1] == movies_df['rating'].iloc[2]):
				franchise_dict['same_rating'] = 0.0
			else:
				franchise_dict['same_rating'] = 1.0

			franchises_dict_list.append(franchise_dict)
		except IndexError:
			print(IndexError)

# collapsed_df = pd.DataFrame(franchises_dict_list)
