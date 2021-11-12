import os
import sys
import geopandas
#from data import dataCompile


watershedFile = 'data/mitigationBank/Mitigation_Bank_Watersheds.geojson'

def test_readCSV():
    fileReadPath = 'data/mitigationBank/Mitigation_Bank_Watersheds.csv'

    file = geopandas.read_file(fileReadPath)

    assert not file.empty

def test_readGEOJSON():
    fileReadPath = 'data/mitigationBank/Mitigation_Bank_Watersheds.geojson'

    file = geopandas.read_file(fileReadPath)

    assert not file.empty

