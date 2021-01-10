# Overview

Generate a DEM using the Canadian Digital Elevation Model (CDEM)
pannels that covering south-west Ontario.  These panels use
NAD83(CSRS) coordinates (a refinement of the NAD83 coordinates).

The CDEM pannels are mostly masked outside of Canada, apart from some
strange square regions include at the great lake levels.  Use the the
CanVec admin boundaries to get rid of these.  The CanVec data uses
NAD83 coordinates.

# Download the data

Get the CDEM panels that cover south-western Ontario.

```bash
for i in {30..31} {40..41}; do
  wget -r -nd ftp://ftp2.cits.rncan.gc.ca/pub/cdem/0$i
done
for i in *.zip; do unzip $i ${i%%_tif.zip}.tif; done
```

Get the CanVec admin boundary files for Ontario.

```
# Need to add the wget command here
unzip ../CanVec/canvec_250K_ON_Admin_shp.zip geo_political_region_2.*
```

# Ideal process

```bash
gdalwarp -of JP2OpenJPEG -co QUALITY=100 -co REVERSIBLE=yes -srcnodata 0 -cutline geo_political_region_2.shp -dstnodata -32768 -te -83.15 41.65 -78.40 45.35 -ts 5700 4440 -t_srs EPSG:4326 cdem_dem_*.tif cdem.jp2
```

Unfortunately `gdalwarp` doesn't support the JP2 output (not too big
of a deal) and the `-cutline` option dies on some (bogus I believe)
self-intersection error forcing us to rasterize a mask layer.

It may be possible to use ``--config GDALWARP_IGNORE_BAD_CUTLINE YES``
to resolve this.

# Actual process

Merge the individual pannels into a single large one in the WGS84
coordinate system covering 300km north, east, south, and west of the
London Soaring Club.  Reduce the resolution to 25% to maintain a
reasonable memory footprint (around 50MB).

```bash
gdalwarp -srcnodata 0 -dstnodata -32768 -t_srs EPSG:4326 -te -83.15 41.65 -78.40 45.35 -ts 5700 4440 cdem_dem_*.tif cdem_merged.tif
```

Clip to the boundary of Canada via an intermediate raster layer.  Size
of the raster layer is determined by running `gdalinfo` on
*cdem_merged.tif*.

```bash
ogr2ogr -t_srs EPSG:4326 cdem_mask.shp geo_political_region_2.shp
gdal_rasterize -burn 1 -l cdem_mask -te -83.15 41.65 -78.40 45.35 -ts 5700 4440 -ot Int16 cdem_mask.shp cdem_mask.tif
gdal_calc.py --calc '(B==1)*A+(B==0)*-32768' --NoDataValue=-32768 -A cdem_merged.tif -B cdem_mask.tif --outfile cdem.tif
```

Convert to a losseless JP2 file.

```bash
gdal_translate -of JP2OpenJPEG -co QUALITY=100 -co REVERSIBLE=yes cdem.tif cdem.jp2
```

# Viewing

The hillshade computation works best with square units.  Build a
maximum resolution version of the CDEM using UTM zone 17N coordinates.

```bash
gdalwarp --config GDALWARP_IGNORE_BAD_CUTLINE YES -of GTiff -srcnodata 0 -cutline geo_political_region_2.shp -dstnodata -32768 -te_srs EPSG:4326 -te -83.15 41.65 -78.40 45.35 -t_srs EPSG:32617 cdem_dem_*.tif cdem_map.tif
```

Use it to compute the hillshade (note that if weren't using UTM
coordinates we would need to use -s to specify the scale between
the horizontal vertical units -- 111120 for degrees -> meters)

```bash
gdaldem hillshade -compute_edges cdem_map.tif hillshade.tif
```

Compute a semi-transparent overlay.  The first value is the computed
hillshade value (220 is flat), the next three are RGB colours, and the
last is transparency (0 is transparent).

```
cat >shade.rmp <<"EOF"
0 0 0 0 255
32 0 0 0 240
64 0 0 0 180
96 0 0 0 120
220 0 0 0 0
221 255 255 255 0
255 255 255 255 192
EOF
gdaldem color-relief -alpha hillshade.tif shade.rmp hillshade_overlay.tif
```
