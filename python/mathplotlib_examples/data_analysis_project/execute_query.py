import psycopg2
import redshift_property as rp

def executeQuery(queryDict):
    conn = psycopg2.connect(rp.prodDbConnection)
    cursor = conn.cursor()

    zipWiseData = {}

    for qTitle in queryDict:

        cursor.execute(queryDict[qTitle])
        rows = cursor.fetchall()
        for row in rows:

            if row[0] != None:
                zipWiseData[row[0]] = (row[1] /492.0) * 25

    cursor.close()
    conn.close()

    return zipWiseData

#-----------------------------------------
# This function only handles one data set
#-----------------------------------------
def executeQuery1(queryDict):
    conn = psycopg2.connect(rp.prodDbConnection)
    cursor = conn.cursor()

    dataDict = {}

    for qTitle in queryDict:
        x = []
        y = []
        cursor.execute(queryDict[qTitle])
        rows = cursor.fetchall()
        for row in rows:

            if row[0] != None:
                x.append(row[1])
                y.append(row[0])

    cursor.close()
    conn.close()
    dataDict['x'] = x
    dataDict['y'] = y
    return dataDict

#-----------------------------------------
#
#-----------------------------------------
def executeQuery2(queryDict):
    conn = psycopg2.connect(rp.prodDbConnection)
    cursor = conn.cursor()

    report = {}

    for qTitle in queryDict:
        x = []
        y = []
        cursor.execute(queryDict[qTitle])
        rows = cursor.fetchall()
        for row in rows:

            if row[0] != None:
                x.append(row[1])
                y.append(row[0])

        report[qTitle] = {"x" : x, "y" : y}

    cursor.close()
    conn.close()
    return report
