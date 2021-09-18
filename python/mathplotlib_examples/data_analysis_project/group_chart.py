import matplotlib.pyplot as plt

myFigure = None

def genGroupChart(x, y, chartLabel, chartNum):
    #plt.close('all')

    global myFigure
    if myFigure == None:
        myFigure = plt.figure(1)



    plt.subplot(chartNum)
    #plt.plot(x, y, label=chartLabel)
    plt.bar(x, y, label=chartLabel)
    plt.legend()


    plt.xlabel('Purchase Amt')

    plt.ylabel('# of Players')
    plt.title(chartLabel)
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([0, 500, 0, 5000])
    plt.grid(True)

    return plt


