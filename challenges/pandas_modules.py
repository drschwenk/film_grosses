
__author__ = 'schwenk'

import pylab
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import dateutil
import dateutil.parser
from collections import defaultdict

'''
['title',
			'domestic_total_gross',
			'release_date',
			'runtime',
			'rating',
			'budget',
			'genre',
			'distrib',
			'oscars'
'''

with open("complete_data.pkl", 'r') as picklefile:
    complete_data_for_pandas = pickle.load(picklefile)


df = pd.DataFrame(complete_data_for_pandas)


# df['domestic_total_gross'].hist()
# plt.title('Histogram of Movies by Box Office Revenues')
# plt.xlabel('Box Office (Billions of Dollars)')
# plt.ylabel('Number of Movies')
# plt.show()

# df['budget'].hist()
# plt.title('Histogram of Movies by Box Office Revenues')
# plt.xlabel('budget (hundreds of milions of Dollars)')
# plt.ylabel('Number of Movies')
# plt.show()

# import matplotlib.pyplot as plt
# plt.scatter(df.budget, df.domestic_total_gross)
# plt.title('How does budget relate to final box office revenue?\n')
# plt.xlabel('Budget')
# plt.ylabel('Box Office')
# plt.show()




sortedbyruntime = df.sort(columns='budget')
# print sortedbyruntime.head()

# releasedateplot = df.plot(x="release_date",y="domestic_total_gross")
# plt.show()

# runtimeplot = sortedbyruntime.scatter(x="release_date",y="domestic_total_gross")
# plt.show()

mydata = sortedbyruntime[["budget", "domestic_total_gross"]].dropna(how="any")
# Now plot with matplotlib
vals = mydata.values
plt.scatter(vals[:, 0], vals[:, 1])
plt.show()


# summed_rating_groups = df.groupby('Rating').sum()
# numberpercat = df.groupby('Rating').size()
# avs = summed_rating_groups.div(numberpercat,axis=0)
#
# rating_groups = df.groupby('Rating')

def makeplot(data):
	# fig, ax = plt.subplots(nrows=4, ncols=1,sharex=True)
	# plt.title('Domestic grosses', fontsize=17);
	# plt.ylabel("Millions of $", fontsize=15, labelpad=15);
	#
	# loopc=0
	# for name, group in rating_groups:
	# 	group.plot(x="ReleaseDate",y="DomesticTotalGross", ax = ax[loopc])
	# 	loopc+=1

	# plt.xlabel("Films", fontsize=15, labelpad=5);
	# plt.axis([0.8,3.2,0,600])
	# plt.xticks(rotation=60)
	# plt.tick_params(axis='x', which='major', labelsize=15)
	# plt.setp(g1_plot, color='c', alpha=0.7, linewidth=3.0)
	# plt.setp(g2_plot, color='m',alpha=0.7, linewidth=3.0)
	# plt.legend([g1_plot, g2_plot],loc='lower left')
	plt.show()


sortedbyruntime = df.sort(columns='Runtime')

# releasedateplot = df.plot(x="ReleaseDate",y="DomesticTotalGross")
# plt.show()

# runtimeplot = sortedbyruntime.plot(x="Runtime",y="DomesticTotalGross")
# plt.show()

summed_rating_groups = df.groupby('Rating').sum()
numberpercat = df.groupby('Rating').size()
avs = summed_rating_groups.div(numberpercat,axis=0)

rating_groups = df.groupby('Rating')

# fig, ax = plt.subplots(nrows=4, ncols=1,sharex=True)
# plt.title('Domestic grosses', fontsize=17);
# plt.ylabel("Millions of $", fontsize=15, labelpad=15);
#
# loopc=0
# for name, group in rating_groups:
# 	group.plot(x="ReleaseDate",y="DomesticTotalGross", ax = ax[loopc])
# 	loopc+=1

# plt.xlabel("Films", fontsize=15, labelpad=5);
# plt.axis([0.8,3.2,0,600])
# plt.xticks(rotation=60)
# plt.tick_params(axis='x', which='major', labelsize=15)
# plt.setp(g1_plot, color='c', alpha=0.7, linewidth=3.0)
# plt.setp(g2_plot, color='m',alpha=0.7, linewidth=3.0)
# plt.legend([g1_plot, g2_plot],loc='lower left')
plt.show()