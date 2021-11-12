import geopandas
import matplotlib.pyplot as plt


def readGeoSave(read_filePath, save_filePath):
    #geojsonPath = 'data/mitigationBank/Mitigation_Bank_Watersheds.geojson'
    geojsonPath = read_filePath

    gdf = geopandas.read_file(geojsonPath)

    # https://geopandas.org/docs/user_guide/interactive_mapping.html
    # https://geopandas.org/gallery/polygon_plotting_with_folium.html
    m = gdf.explore(column="SHAPEAREA",
                    tooltip='NAME',
                    tiles="Carto DB positron",
                    cmap='Pastel1',
                    legend=False)
    #m.save("demo/foliumMap.html")
    m.save(save_filePath)

