import mpl_toolkits
mpl_toolkits.__path__.append('/Library/Python/2.7/site-packages/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from plotly.offline import offline
import plotly.tools as tls
import plotly.plotly as py


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
        #plt.plot(x, y)

    plt.legend(loc=0)
    fig.autofmt_xdate()
    plt.title(chartName)
    plt.savefig(chartName + '.png')

def plotBarChart(dataList, chartName):
    numPlots = 10
    colorMap = plt.cm.gist_ncar
    plt.gca().set_color_cycle([colorMap(i) for i in np.linspace(0, 0.9, numPlots)])

    fig, ax = plt.subplots(1)

    for d in dataList:
        y = dataList[d]['x']
        x = dataList[d]['y']
        plt.plot(x, y, label=d)
        #plt.plot(x, y)

    plt.legend(loc=0)
    fig.autofmt_xdate()
    plt.title(chartName)
    plt.savefig(chartName + '.png')

def testPlotlyOffline():
    #import matplotlib.pyplot as plt
    #import numpy as np

    #import plotly.plotly as py
    #import plotly.tools as tls
    # Learn about API authentication here: https://plot.ly/python/getting-started
    # Find your api_key here: https://plot.ly/settings/api

    mpl_fig = plt.figure()
    ax = mpl_fig.add_subplot(111)

    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = ax.bar(ind, menMeans, width, color=(0.2588, 0.4433, 1.0))
    p2 = ax.bar(ind, womenMeans, width, color=(1.0, 0.5, 0.62),
                bottom=menMeans)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Groups')
    ax.set_title('Scores by group and gender')

    ax.set_xticks(ind + width / 2.)
    ax.set_yticks(np.arange(0, 81, 10))
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

    plotly_fig = tls.mpl_to_plotly(mpl_fig)

    # For Legend
    plotly_fig["layout"]["showlegend"] = True
    plotly_fig["data"][0]["name"] = "Men"
    plotly_fig["data"][1]["name"] = "Women"

    #plot_url = py.plot(plotly_fig, filename='stacked-bar-chart')

    plot_url = offline.plot(plotly_fig, filename='stacked-bar-chart.png')

def testBarGraphs(chartData, chartTitle, xLable, yLable):
    myColor = ['r', 'b', 'g', 'yellow', 'maroon']
    numPlots = 10
    colorMap = plt.cm.gist_ncar
    plt.gca().set_color_cycle([colorMap(i) for i in np.linspace(0, 0.9, numPlots)])

    myKeys = [k for k in chartData.keys()]
    dates = [d for k in chartData.keys() for d in chartData[k].keys()]
    datesSorted = sorted(list(set(dates)))
    y_pos = np.arange(len(datesSorted))
    bar_width = 0.30
    #bar_width = 1.0
    opacity = 0.8
    numCountries = len(chartData[myKeys[0]][datesSorted[0]])

    for j in xrange(numCountries):
        valueList = []
        c = None
        for i, d in enumerate(datesSorted):
            c = chartData[myKeys[0]][d][j][0]
            v = chartData[myKeys[0]][d][j][1]
            valueList.append(v)
        print valueList
        print j
        plt.bar(y_pos + (bar_width * j), valueList, bar_width, alpha=opacity, color=myColor[j], label=c)

    plt.legend(loc=0)
    plt.xlabel(xLable)
    plt.ylabel(yLable)
    plt.title(chartTitle)
    plt.xticks(y_pos + ((bar_width * len(datesSorted))/2 ), datesSorted)
    plt.savefig('test.png')
    exit()


    day1 = (20, 35, 30, 35, 27)
    day2 = (25, 32, 34, 20, 25)

    N = len(day1)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    #rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
    rects1 = ax.bar(ind, day1, width )

    #rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)
    rects2 = ax.bar(ind + width, day2, width )

    # add some text for labels, title and axes ticks
    ax.set_ylabel('# of players')
    ax.set_title('Top 5 countries by install')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

    ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    plt.savefig('test.png')

def stackBarGraphs(chartData, chartTitle, xLable, yLable):
    colorDict = { 'b' : 'blue', 'g' : 'green', 'r' : 'red', 'c' : 'cyan', 'm' : 'magenta', 'y' : 'yellow', 'k' : 'black', 'w' : 'white' }
    myColor = ['r', 'b', 'g', 'yellow', 'maroon']
    numPlots = 10
    colorMap = plt.cm.gist_ncar
    plt.gca().set_color_cycle([colorMap(i) for i in np.linspace(0, 0.9, numPlots)])

    fig, ax = plt.subplots(1)
    myKeys = [k for k in chartData.keys()]
    xCordinates = [d for k in chartData.keys() for d in chartData[k].keys()]
    xCordinatesSorted = sorted(list(set(xCordinates)))
    yPos = np.arange(len(xCordinatesSorted))

    bar_width = 0.30
    opacity = 0.8

    xValues = len(chartData[myKeys[0]][xCordinatesSorted[0]])
    stackedValues = [0*i for i in xrange(len(xCordinatesSorted))]

    for j in xrange(xValues):
        valueList = []
        c = None

        for i, d in enumerate(xCordinatesSorted):
            c = chartData[myKeys[0]][d][j][0]
            v = chartData[myKeys[0]][d][j][1]
            valueList.append(v)

        #plt.bar(yPos, valueList, bar_width, bottom=stackedValues, alpha=opacity, color=myColor[j], align='center', label=c)
        plt.bar(yPos, valueList, bar_width, bottom=stackedValues, alpha=opacity, align='center', label=c)
        stackedValues = [m+n for m, n in zip(stackedValues, valueList)]

    fig.autofmt_xdate()
    plt.legend(loc=0)
    plt.xlabel(xLable)
    plt.ylabel(yLable)
    plt.title(chartTitle)
    plt.xticks(yPos, xCordinatesSorted)
    plt.savefig('test.png')
