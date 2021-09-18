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

churnPlayerData = eq.executeQuery1(dq.listOfChurnPlayers)
notChurnPlayerData = eq.executeQuery1(dq.listOfNotChurnPlayers)

dataList = []
dataList.append(notChurnPlayerData)
dataList.append(churnPlayerData)

gc.plotScatterChart(dataList, 'ChurnAndNotChurnPlayers')




