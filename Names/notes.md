```
wget -d ftp://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/geobase_cgn_toponyme/prov_shp_eng/cgn_on_shp_eng.zip
```

The `rel_scale` entry does a good job at separting items into layers. Use all `category` except `Administrative
Area` as that does not apply particularly well to a point and would ideally be hidden at higher zoom levels.

* Administrative Area - mostly don't want as areas, maybe do want reservations
* Constructed Feature - a lot of drains, probably want rest which includes dams, forces bases, and such
* Feature Assoicatied with Vegetation - mostly swamps and wetlands, maybe want
* Populated Place - towns, citys, and such, do want
* Terrain Feature - hills, ridges, canyons, reefs, and such
* Underground Feature - one cave system feature, might as well include
* Undersea and Maritime Feature - one niagra fan feature, might as well include
* Water Feature - lakes, rivers, and such, do want

Some entries, such as forces bases and the great lakes, have an English and a French entry on top of each
other. There doesn't seem to be a good way to distinguish between the two from the names database itself.  The
[*english.py*](english.py) python code in this directory will go through the *cgn_on_shp_eng.shp* shape file and
drop all but the most English (as measured by the probability of being English vs French as computed by the NLTK
TextCat classifier) of all entries with a common geometry. This seems to work well in practice.
