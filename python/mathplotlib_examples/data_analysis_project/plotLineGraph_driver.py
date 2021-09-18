import numpy as np
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import psycopg2
import redshift_property as rp
import dbquery as dq
import group_chart as gc
import mpl_toolkits
mpl_toolkits.__path__.append('/Library/Python/2.7/site-packages/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap
import util
import generate_charts as gc
import execute_query as eq

#lineChart = eq.executeQuery2(dq.activeInactivePlayerStats)
#lineChart = eq.executeQuery2(dq.activeInactivePlayerLevel)
lineChart = eq.executeQuery2(dq.activeInactivePlayerSessions)

for i in lineChart:
    print lineChart[i]['x']
    print lineChart[i]['y']

#gc.plotLineChart(lineChart, 'Length of Play on Day of Install')
#gc.plotLineChart(lineChart, 'Level Reached on Day of Install')
gc.plotLineChart(lineChart, '# of Sessions on the Day of Install')
