import geopandas


points = geopandas.read_file('centroidPoints.geojson')
watershed = geopandas.read_file('mitigationBank/Mitigation_Bank_Watersheds.geojson')

locWater = []

print("Beginning poly coding")
for _, rowPoint in points.iterrows():
    print(f"Working on row {rowPoint.OBJECTID}")
    found = False
    for _, rowWater in watershed.iterrows():
        if rowPoint.geometry.within(rowWater.geometry):
            locWater.append(rowWater.NAME)
            found = True
            break
    if not found:
        locWater.append('')


        
