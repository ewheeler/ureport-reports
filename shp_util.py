import operator
import itertools

import ogr

ogrdriver = ogr.GetDriverByName("ESRI Shapefile")
shape = ogrdriver.Open("Uganda_districts2010.shp")

shape.GetLayerCount()
layer = shape.GetLayerByIndex(0)

layer.GetFeatureCount()
features = [layer.GetFeature(n) for n in xrange(layer.GetFeatureCount())]

feature_keys = set(list(itertools.chain.from_iterable([f.keys() for f in features])))

names2010 = map(operator.attrgetter('DNAME_2010'), features)
names2006 = map(operator.attrgetter('DNAME_2006'), features)

district_names = [(f['DNAME_2006'], f['DNAME_2010']) for f in features]
changed_names = [t for t in district_names if t[0] != t[1]]

set(names2010).difference(names2006)
