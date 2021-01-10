This is an initial dump of my personal notes I made when creating alternative maps for government data sources for
the open source XCSoar program for the London Soaring Club (south-western Ontario).

The reason I created these maps is I was interested in playing around with the open-source GIS programs, and the
standard OpenStreetMap based maps had some issues, including at least

- not doing a great job on classifying road levels,
- not doing a great job at marking the edges of urban areas, and
- not doing a great job on water.

This last one was especially notable as the OpenStreeMap based ones missed Wildwood lake, which is a large dammed
water body to the north of the London Soaring Club that is quite useful for locating yourself. I initially looked
into just fixing this (IIRC, it was due to the conversion program not properly handling the older OpenStreetMap way
of declaring water), but in the end decided creating my own maps would be more interesting.

For the maps, I used a variety of government data sources. Specifically

- Canadian Digital Elevation Model (CDEM)
- Topographical Data of Canada (CanVec) Ontario versions
- Canadian Geographical Names Database
- StatsCan Population Centres and Designated Places

plus that standard airspace and way point files found online.

The following are my raw notes on processing these various data sources

- [AirSpace](AirSpace/notes.md)
- [CDEM](CDEM/notes.md)
- [CanVec](CanVec/notes.md)
- [Names](Names/notes.md)
- [StatsCan](StatsCan/notes.md)

plus my high-level notes on putting it all together

- [Notes](notes.md)

Hopefully I will get a chance to clean this up into something a bit easier to follow at some point. In the
meantime, you can find the final results in the XCSoar folder. To use

- zip up all the files in `XCSoar` (don't include the directory)

```
cd XCSoar
zip -9 ontario.zip *
```

- rename the `zip` file to a `xcm` file

```
mv ontario.zip ontario.xcm
```

- upload it to your XCSoar device and pick it as the map
