import geopandas
import matplotlib.pyplot as plt


geojsonPath = 'data/mitigationBank/Mitigation_Bank_Watersheds.geojson'

gdf = geopandas.read_file(geojsonPath)

# https://geopandas.org/docs/user_guide/interactive_mapping.html
# https://geopandas.org/gallery/polygon_plotting_with_folium.html
m = gdf.explore(column="SHAPEAREA",
                tooltip='NAME',
                tiles="Carto DB positron",
                cmap='Pastel1',
                legend=False)
m.save("demo/foliumMap.html")

