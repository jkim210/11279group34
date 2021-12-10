import geopandas


#gdf = geopandas.read_file("land_use_cover/Statewide_Land_Use_Land_Cover.geojson")
gdf = geopandas.read_file("landscapeDevelopmentIndex/Current_Landuse_-_Landscape_Development_Intensity_(LDI).geojson")
gdf.to_crs(epsg=3395, inplace=True) #(not sure if step is needed?)
gdf['centroids'] = gdf.centroid

# Pull water parcels
waterIds = [5120,5100,5110,5200,5300,5250,5400,5430,5600,6100,5710,5420,5410,
                                            6120,6130,6150,6149,6170,6159,6179,6210,6180,6189,6182,6220,6216,
                                            6250,6259,6410,6400,6420,6430,6411,6440,6460,6469,6510,6520]
water = gdf.loc[gdf["LEVEL3_VALUE"].isin(waterIds)]

#how to make new geodataframe with just centroid
# spits it out as file
df = gdf[["OBJECTID","centroids"]]
gdf2 = geopandas.GeoDataFrame(df, crs="EPSG:3395", geometry=df.centroids)
gdf2=gdf2.drop(columns="centroids") #-> most important probably
gdf2.to_file("centroidPoints.geojson", driver="GeoJSON")

# not sure what this does acctually
water = water.drop(columns = "geometry")
water['geometry']=water.centroids
water = water.drop(columns="centroids")
water=water.drop(columns="SHAPEAREA")
water=water.drop(columns="SHAPELEN")
unary_union = water.unary_union


#export command not working

