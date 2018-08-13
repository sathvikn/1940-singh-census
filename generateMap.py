import geoplotlib

data = geoplotlib.utils.read_csv('coords.csv')
geoplotlib.dot(data)
geoplotlib.show()


