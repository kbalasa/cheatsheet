import mpl_toolkits
mpl_toolkits.__path__.append('/Library/Python/2.7/site-packages/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def plotOnUSAMap(latLon, zipWiseData, title):
    print zipWiseData
    m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
                projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    # draw coastlines, state and country boundaries, edge of map.
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    for zipcode in zipWiseData:
        try:
            x, y = m(latLon[zipcode]['lon'], latLon[zipcode]['lat'])
            m.plot(x, y, 'bo', markersize=zipWiseData[zipcode])
            print zipcode
            #plt.text(x, y, latLon[zipcode]['city'])
        except KeyError as e:
            print "missing zipcode: " + e.message

    plt.title(title)
    plt.savefig('usa_map_test.png')

def plotOnWorldMap(latLon, countryWiseData, title):
    #m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    #m.fillcontinents(color='coral', lake_color='aqua')
    # draw parallels and meridians.
    #m.drawparallels(np.arange(-90., 91., 30.))
    #m.drawmeridians(np.arange(-180., 181., 60.))

    #m.drawmapboundary(fill_color='aqua')
    for key in countryWiseData:
        try:
            x, y = m(latLon[key]['lon'], latLon[key]['lat'])
            m.plot(x, y, 'bo', markersize=countryWiseData[key])
            plt.text(x, y, countryWiseData[key])
        except KeyError as e:
            print "missing zipcode: " + e.message

    plt.title(title)
    plt.savefig('world_map_test.png')

def plotScatterChart(dataList, chartName):
    #plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    c = ['r', 'b', 'o']
    xticks = []
    i = 0
    for j in range(0,30):
       xticks.append(j)
    plt.xticks(xticks, xticks)
    for d in dataList:
        x = d['x']
        y = d['y']

        plt.scatter(x, y, c=c[i])
        i += 1

    plt.savefig(chartName + '.png')

def plotLineChart(dataList, chartName):
    numPlots = 10
    colorMap = plt.cm.gist_ncar
    plt.gca().set_color_cycle([colorMap(i) for i in np.linspace(0, 0.9, numPlots)])

    fig, ax = plt.subplots(1)

    for d in dataList:
        y = dataList[d]['x']
        x = dataList[d]['y']
        plt.plot(x, y, label=d)

    plt.legend(loc=0)
    fig.autofmt_xdate()
    plt.title(chartName)
    plt.savefig(chartName + '.png')
