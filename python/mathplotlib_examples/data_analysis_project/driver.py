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


latLon = util.getZipcodeWiseGeoLocation() # read latitude and longitude for us zipcodes
#latLon = util.getCountryWiseGeoLocation() # read latitude and longitude for countries

zipWiseData = eq.executeQuery(dq.zipcodeWiseMeanSpending)

gc.plotOnUSAMap(latLon, zipWiseData, 'title')
#gc.plotOnWorldMap(latLon, zipWiseData)

exit()

conn = psycopg2.connect(rp.prodDbConnection);
cursor = conn.cursor();

i = 211
myPlot = None
for k in dq.dailyUserCountByPurchaseAmt:
    cursor.execute(dq.dailyUserCountByPurchaseAmt[k]);
    rows = cursor.fetchall()
    x = []
    y = []
    for row in rows:
        x.append(row[0])
        y.append(row[1])

    myPlot = gc.genGroupChart(x, y, k, i)
    i += 1
myPlot.legend()
myPlot.tight_layout()
myPlot.savefig('test.png')

exit()

#fig, chart = plt.subplots(2,2, sharex=True, sharey=True)
clist = []
# for c in chart:
#     for i in c:
#         clist.append(i)
i = 0
for k in dq.dailyUserCountByPurchaseAmt:
    cursor.execute(dq.dailyUserCountByPurchaseAmt[k]);
    rows = cursor.fetchall()
    x = []
    y = []
    for row in rows:
        x.append(row[0])
        y.append(row[1])

    #clist[i].plot(x, y, label=k)
    #clist[i].set_title(k)

    #i += 1

    plt.plot(x, y, label=k)
    # plt.legend()
    # plt.xlabel('Currency Value')
    # plt.ylabel('Unique Users')
    # plt.grid(True)
    plt.legend()
    plt.savefig(k + '.png')

