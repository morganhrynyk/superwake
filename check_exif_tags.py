import os
from exiftool import ExifToolHelper
import pandas as pd

# Check for exiftool
scriptPath = os.path.realpath(__file__)
exifToolPath = os.path.join(os.path.dirname(scriptPath), 'exiftool.exe')


def getExif(filepath, selectedTags=None):
    exif = {}
    with ExifToolHelper(exifToolPath) as et:
        if selectedTags:
            exif = et.get_tags(filepath, selectedTags)[0]  # et gives list of dicts
        else:
            exif = et.get_metadata(filepath)[0]  # et gives list of dicts
    return exif

with ExifToolHelper() as et:
    print(et.get_tags(r'Y:\Superwake\Shoreline\BC_shoreline\03_bc_shoreline_working\example_imgs\DSC00029.jpg', tags='GPSLatitude'))

#exif = getExif(r'Y:\Superwake\Shoreline\BC_shoreline\03_bc_shoreline_working\example_imgs\DSC00029.jpg')
#df = pd.DataFrame([exif])
#print(df.columns.tolist())