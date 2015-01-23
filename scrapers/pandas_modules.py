
__author__ = 'schwenk'

import pylab
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import dateutil
import dateutil.parser
from collections import defaultdict


with open("complete_data.pkl", 'r') as picklefile:
    complete_data_for_pandas = pickle.load(picklefile)


df = pd.DataFrame(complete_data_for_pandas)

print df.head()

# sortedbyruntime = df.sort(columns='Runtime')

# releasedateplot = df.plot(x="ReleaseDate",y="DomesticTotalGross")
# plt.show()

# runtimeplot = sortedbyruntime.plot(x="Runtime",y="DomesticTotalGross")
# plt.show()

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