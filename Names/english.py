# nix run '(with import <nixpkgs> {}; python3.withPackages (pp: with pp; [ gdal nltk regex ]))'

import nltk
import osgeo.ogr


# English vs French classification using trigram distances to give P(English)

nltk.download('crubadan', quiet=True)
nltk.download('punkt', quiet=True)
classify = nltk.textcat.TextCat()

def probabilityEnglish(name):
  profile = classify.profile(name)
  ranking = [ sum((classify.calc_dist(lang,trigram,profile)
                   for trigram in profile))
              for lang in ('eng','fra') ]
  return (ranking[1] / (ranking[0] + ranking[1]))


# Load in layer

driver = osgeo.ogr.GetDriverByName('ESRI Shapefile')
data = driver.Open('cgn_on_shp_eng.shp',1)
layer = data[0];


# Record FIDs of less-probable-to-be-English duplicate geoemtry

fids = []
features = { }                                   # Most English feature for each seen WKT geometry
for feature in layer:
  geometry = feature.geometry().ExportToWkb()
  if geometry in features:                         # Resolve WKT collision by taking most English feature as ranked by probabilityEnglish
    ranking = sorted([feature,features[geometry]], key=lambda feature: probabilityEnglish(feature['GEONAME']))
    print("Will drop:", ranking[0]['GEONAME'])
    fids.append(ranking[0].GetFID())
    feature = ranking[1]
  features[geometry] = feature
del features


# Remove non-English duplicates (done separate as support for modification while iterating not guaranteed)

for fid in fids:
  layer.DeleteFeature(fid)
