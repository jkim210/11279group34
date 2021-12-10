import geopandas as gdp
import folium
import matplotlib.pyplot as plt
import numpy as np


geojsonPath = 'data/parcelsInNorthern_Ocklawaha.geojson'

parcels = gdp.read_file(geojsonPath)

waterParcels = parcels.loc[parcels['dist'] == 0]
parcels.drop(waterParcels.index, inplace=True)

parcels.drop(parcels.loc[parcels['WATERDISTANCE/LDI'] == 0].index, inplace=True)
parcels.drop(parcels.loc[parcels['WATERDISTANCE/LDI'] > 750].index, inplace=True)

parcels['normalized'] = np.log(parcels['WATERDISTANCE/LDI']) * 15

# https://geopandas.org/docs/user_guide/interactive_mapping.html
# https://geopandas.org/gallery/polygon_plotting_with_folium.html
fMap = folium.Map(location=[29.648, -82.343], zoom_start=14, tiles='CartoDB positron')

m = parcels.explore(column="normalized",
                m=fMap,
                tooltip=['DESCRIPTION', 'OBJECTID', 'normalized'],
                tooltip_kwds={'aliases': ['Description', 
                                        'Parcel ID', 
                                        'Development Impact Value']},
                tiles="Carto DB positron",
                cmap='Reds',
                legend=True,
                legend_kwds={'caption': 'Development Impact (Scaled Logarithmic)'
                            }
                )

folium.features.GeoJson(waterParcels, 
                name="Water Parcels",
                tooltip=folium.features.GeoJsonTooltip(
                    fields=['DESCRIPTION', 'OBJECTID'],
                    aliases = ['Description', 'Water Parcel ID'],
                    labels=True,
                    )
).add_to(m)
folium.LayerControl().add_to(m)

m.save("data/map7.html")

