import geopandas as gdp
import folium
import numpy as np
import os
import webbrowser


def conductDataManipulation(changes):
    geojsonPath = 'data/parcelsInNorthern_Ocklawaha.geojson'
    parcels = gdp.read_file(geojsonPath)

    # Creating parcel dataframes
    waterParcels = parcels.loc[parcels['dist'] == 0]
    parcels.drop(waterParcels.index, inplace=True)

    parcels.drop(parcels.loc[parcels['WATERDISTANCE/LDI'] == 0].index, inplace=True)
    parcels.drop(parcels.loc[parcels['WATERDISTANCE/LDI'] > 750].index, inplace=True)

    parcels['normalized'] = np.log(parcels['WATERDISTANCE/LDI']) * 15

    # Get unique lvl 3 values
    uniques = parcels.drop_duplicates('LEVEL3_VALUE').drop(['OBJECTID', 'SHAPEAREA', 'nearestID', 'dist', 'geometry', 'WATERDISTANCE/LDI', 'normalized'], axis=1)
    uniques.set_index('LEVEL3_VALUE', inplace=True)

    def formula(dist, LSI):
        if LSI != 0:
            return dist / LSI
        else:
            return 0

    # Take in changes
    for change in changes:
        parcelID, lvl3 = change
        parcels.loc[parcels['OBJECTID'] == parcelID, ['LEVEL3_VALUE', 'LDI', 'LSI', 'DESCRIPTION']] = [lvl3] + uniques.loc[lvl3].values.tolist()

    if len(changes) > 0:
        parcels['WATERDISTANCE/LDI'] = parcels.apply(lambda row: formula(row.dist, row.LSI), axis=1)
        parcels['normalized'] = np.log(parcels['WATERDISTANCE/LDI']) * 15

    return [parcels, waterParcels]

def createMap(parcels, waterParcels):
    # Create map
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

    m.save("map.html")

def openFile(filePath):
    webbrowser.open_new('file://' + os.path.realpath(filePath))

if __name__ == "__main__":
    allChanges = []

    while(True):
        try:
            openFile('map.html')
        except:
            pass

        # Take options
        # Change parcel dev, Print info for area, Undo all changes
        userOption = input("  - Change parcel development (0)\n  - Undo changes (1)\n  - Exit (2)\n->") 

        # Changing parcel dev
        if userOption == '0':
            userParcelID = int(input("Select parcel by inputting id: "))
            openFile('data/uniques.html')
            userParcelVal = int(input("Select parcel type by inputting LEVEL3 value: "))
            # check if parcel is valid and if proper lvl3
            userChange = [userParcelID, userParcelVal]
            allChanges.append(userChange)

            p, water = conductDataManipulation(allChanges)
            createMap(p, water)

            print("Map compilation finished - displaying map")
        elif userOption == '1':
            createMap(conductDataManipulation([]))
            print("Map compilation finished - displaying map")

        elif userOption == '2':
            break
        else:
            print("Improper input")