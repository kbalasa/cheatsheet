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

zipdict = util.getZipcodeWiseGeoLocation()

conn = psycopg2.connect(rp.prodDbConnection);
cursor = conn.cursor();

zipcodeCount = {}
for k in dq.zipcodeWiseSpendersAbove10000:
    cursor.execute(dq.zipcodeWiseSpendersAbove10000[k]);
    rows = cursor.fetchall()
    for row in rows:
        if row[0] != None:
            zipcodeCount[row[0]] = (row[1] /1.0) * 25

# m = Basemap(projection='stere',lon_0=lon_0,lat_0=90.,lat_ts=lat_0,\
#             llcrnrlat=latcorners[0],urcrnrlat=latcorners[2],\
#             llcrnrlon=loncorners[0],urcrnrlon=loncorners[2],\
#             rsphere=6371200.,resolution='l',area_thresh=10000)

m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()

for code in zipcodeCount:
    print code
    try:
        x, y = m(zipdict[code]['lon'], zipdict[code]['lat'])
        m.plot(x, y, 'bo', markersize=zipcodeCount[code])
    except:
        print "missing zipcode"

plt.savefig('test.png')
exit()




map = Basemap(projection='cyl')

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
plt.savefig('test.png')
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
cursor.close()
conn.close()
exit()


