import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import folium


#geojsonPath = 'data/mitigationBank/Mitigation_Bank_Watersheds.geojson'
#geojsonPath = 'data/landuseLDI_centroids_nearestID_dist.geojson'

#gdf = geopandas.read_file(geojsonPath)

# https://geopandas.org/docs/user_guide/interactive_mapping.html
# https://geopandas.org/gallery/polygon_plotting_with_folium.html
'''
m = gdf.explore(column="SHAPEAREA",
                tooltip='NAME',
                tiles="Carto DB positron",
                cmap='Pastel1',
                legend=False)
m.save("demo/foliumMap.html")
'''

import random

watershed = geopandas.read_file('data/mitigationBank/Mitigation_Bank_Watersheds.geojson')
#centroids = geopandas.read_file('centroidPoints.geojson')
parcels = geopandas.read_file('data/REDUCEDlanduseLDI_centroids_nearestID_dist.geojson')

drops = []
for i in range(len(parcels.index)):
  if random.random() > .08:
    drops.append(i)

reducedParcels = parcels.drop(drops)
print(reducedParcels)

m = folium.Map(location=[27.70, -82.94], zoom_start=7, tiles='CartoDB positron')
folium_watersheds = folium.features.GeoJson(watershed, name="Watersheds")
#file = open("REDUCEDx2landuseLDI_centroids_nearestID_dist.geojson")
folium_parcels = folium.features.GeoJson(reducedParcels, folium.features.GeoJsonTooltip(
    fields=['LDI', 'DESCRIPTION', 'LSIxWATERDISTANCE']
), name="Parcels")

m.add_child(folium_watersheds)
m.add_child(folium_parcels)
folium.LayerControl().add_to(m)
m.save('map3.html')
