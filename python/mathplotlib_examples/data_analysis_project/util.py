
def getZipcodeWiseGeoLocation():
    import csv
    zipdict = {}
    #f = open('uszipcode.txt', 'r')
    f = open('zipcode_data/zipcode.csv', 'r')
    f = csv.reader(f)
    i=0
    for r in f:
        l = len(r)
        if i != 0 and l == 7:
            zipdict[r[0]] = {'lat': float(r[3]), 'lon': float(r[4]), 'city': r[1]}
        i += 1

    return zipdict

def getCountryWiseGeoLocation():
    import csv
    geoLoc = {}
    #f = open('uszipcode.txt', 'r')
    f = open('zipcode_data/country_wise_geo_cordinate.csv', 'r')
    f = csv.reader(f)
    i=0
    for r in f:
        if i != 0:
            try:
                geoLoc[r[0]] = {'lat': float(r[1]), 'lon': float(r[2])}
            except ValueError as e:
                print r
        i += 1

    return geoLoc
