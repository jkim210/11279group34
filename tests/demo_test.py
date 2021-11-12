import os
import sys
import geopandas
from demo import demo


watershedFile = 'data/mitigationBank/Mitigation_Bank_Watersheds.geojson'

def test_createMap():
    saveFile_path = 'demo/demoMap.html'

    demo.readGeoSave(watershedFile, saveFile_path)

    assert os.path.exists(saveFile_path)

    if(os.path.exists(saveFile_path)):
        os.remove(saveFile_path)

def test_createMapFail():
    saveFile_path = 'demo/demoMap.html'

    assert not os.path.exists(saveFile_path)

    if(os.path.exists(saveFile_path)):
        os.remove(saveFile_path)

def test_fileRead():
    gdf = geopandas.read_file(watershedFile)

    assert not gdf.empty
