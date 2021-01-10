MemTotal:         249884 kB
MemFree:          199752 kB

zoom levels
  layer is displayed if min screen distance < 8 * specified range (all in km)

  1 zoom is about 41% increase (doubles every 2 zooms)

  2 zoom - about 48nm
  4 zoom - about 24nm
  6 zoom - about 12nm

  100 - 0 zooms
  10  - 3 zooms
  1   - 9 zooms

  only every nth polygon point is used according to the following

  min screen distance > 6 * specified range => 4
  min screen distance > 4 * specified range => 3
  min screen distance > 2 * specified range => 2
  otherwise                                 => 1


canvec_250K_ON_Admin_shp.zip
  geo_political_region_2.shp
canvec_250K_ON_Elevation_shp.zip
  contour_1.shp
  elevation_point_0.shp
canvec_250K_ON_Hydro_shp.zip
  hydro_obstacle_0.shp
  hydro_obstacle_1.shp
  hydro_obstacle_2.shp
  waterbody_2.shp
  watercourse_1.shp
canvec_250K_ON_Land_shp.zip
  cut_line_1.shp
  landform_feature_1.shp
  landform_feature_2.shp
  saturated_soil_2.shp
  shoreline_1.shp
  wooded_area_2.shp
canvec_250K_ON_ManMade_shp.zip
  building_0.shp
  chimney_0.shp
  dam_0.shp
  dam_1.shp
  dam_2.shp
  leisure_area_0.shp
  liquid_storage_facility_2.shp
  protection_structure_1.shp
  residential_area_0.shp
  residential_area_2.shp
  ritual_cultural_area_0.shp
  sewage_pipeline_1.shp
  tank_0.shp
  tower_0.shp
  waste_2.shp
canvec_250K_ON_Res_MGT_shp.zip
  aggregate_2.shp
  communication_line_1.shp
  oil_gas_site_0.shp
  ore_0.shp
  ore_2.shp
  pipeline_1.shp
  power_line_1.shp
  transformer_station_0.shp
canvec_250K_ON_Transport_shp.zip
  nautical_facility_1.shp
  navigational_aid_0.shp
  railway_station_0.shp
  road_ferry_1.shp
  road_segment_1.shp
  runway_0.shp
  track_segment_1.shp
  track_structure_1.shp
  trail_0.shp
  trail_1.shp

WOODAREA.zip
  WOODED_AREA.shp

cdem
gpc_000b11a_e     (population centres)
gdpl000b11a_e     (designated places)
watercourse_1_2
waterbody_2_2     "name_en" is not null or "namelk1en" is not null or "namelk2en" is not null or "namerv1en" is not null or "namerv2en" is not null
watercourse_1_2   "name_en" is null and "name_1_end" is null and "name_2_end" is null
road_segment_1_2  "rdcls_en" in ('Expressway-Highway','Freeway')
road_segment_1_3  "rdcls_en" in ('Expressway-Highway','Freeway')
road_segment_1_2  "rdcls_en" in ('Collector','Arterial','Service Lane','Ramp')
road_segment_1_3  "rdcls_en" in ('Collector','Arterial','Service Lane','Ramp')
road_segment_1_2  "rdcls_en" in ('Rapid Transit','Local-Strata','Local-Street','Local-Unknown','Alleyway-Lane')
road_segment_1_3  "rdcls_en" in ('Rapid Transit','Local-Strata','Local-Street','Local-Unknown','Alleyway-Lane')
track_segment_1
cgn_on_shp_eng "category" not in ('Administrative Area') and "rel_scale" in ('2000000','5000000','7500000','15000000','30000000')
cgn_on_shp_eng "category" not in ('Administrative Area') and "rel_scale" in ('1000000')
cgn_on_shp_eng "category" not in ('Administrative Area') and "rel_scale" in ('250000')
bdg_named_feature_0 "namdesc_en" in ('City','city-City')
bdg_named_feature_0 "namdesc_en" in ('Town','town-Town')
bdg_named_feature_0 "namdesc_en" in ('Village','vilg-Village')
bdg_named_feature_0 "namdesc_en" in ('Unincorporated place','unp-Unincorporated Place','unp-Unincorporated place')

unzip gpc_000b11a_e.zip 'gpc_000b11a_e.*'
unzip gdpl000b11a_e.zip 'gdpl000b11a_e.*'
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from gpc_000b11a_e" popcenter.shp gpc_000b11a_e.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from gdpl000b11a_e" desplace.shp gdpl000b11a_e.shp

unzip canvec_250K_ON_Hydro_shp.zip 'waterbody_2.*' 'watercourse_1.*'
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from waterbody_2" waterbody.shp waterbody_2.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from watercourse_1" watercourse.shp watercourse_1.shp

unzip canvec_250K_ON_Transport_shp.zip 'road_segment_1.*' 'track_segment_1.*'
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from road_segment_1 where rdcls_en in ('Expressway-Highway','Freeway')" road_1.shp road_segment_1.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from road_segment_1 where rdcls_en in ('Collector','Arterial','Service Lane','Ramp')" road_2.shp road_segment_1.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from road_segment_1 where rdcls_en in ('Rapid Transit','Local-Strata','Local-Street','Local-Unknown','Alleyway-Lane')" road_3.shp road_segment_1.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select 0 from track_segment_1" track.shp track_segment_1.shp

unzip cgn_on_shp_eng.zip
unzip canvec_50K_ON_Toponymy_shp.zip 'bdg_named_feature_0.*'
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select geoname from cgn_on_shp_eng where category not in ('Administrative Area') and rel_scale in ('2000000','5000000','7500000','15000000','30000000')" place_1.shp cgn_on_shp_eng.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select geoname from cgn_on_shp_eng where category not in ('Administrative Area') and rel_scale in ('1000000')" place_2.shp cgn_on_shp_eng.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select geoname from cgn_on_shp_eng where category not in ('Administrative Area') and rel_scale in ('250000')" place_3.shp cgn_on_shp_eng.shp

ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select name_en from bdg_named_feature_0 where namdesc_en in ('City','city-City')" place_1.shp bdg_named_feature_0.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select name_en from bdg_named_feature_0 where namdesc_en in ('Town','town-Town')" place_2.shp bdg_named_feature_0.shp
ogr2ogr -t_srs EPSG:4326 -clipdst -83.15 41.65 -78.40 45.35 -sql "select name_en from bdg_named_feature_0 where namdesc_en in ('Village','vilg-Village','Unincorporated place','unp-Unincorporated Place','unp-Unincorporated place')" place_3.shp bdg_named_feature_0.shp
