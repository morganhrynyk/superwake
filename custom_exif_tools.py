# exif taggs: https://exiftool.org/TagNames/GPS.html

import os, csv
from exiftool import ExifToolHelper

# Check for exiftool
scriptPath = os.path.realpath(__file__)
exifToolPath = os.path.join(os.path.dirname(scriptPath), 'exiftool.exe')


def get_img_tuples(folder_path):
    jpg_tuples = [(file.split('.')[0], os.path.join(folder_path, file)) for file in os.listdir(folder_path) if
                  file.lower().endswith('.jpg')]
    return jpg_tuples


def get_gps_dict(csv_file_path):
    gps_dict = {}

    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            image_name = row['# image name'].split('.')[0]  # Stripping '.jpg'
            latitude = float(row['latitude [decimal degrees]'])
            longitude = float(row['longitude [decimal degrees]'])
            altitude = float(row['altitude [meter]'])
            roll = float(row['roll [degrees]'])
            pitch = float(row['pitch [degrees]'])
            yaw = float(row['yaw [degrees]'])
            # Creating the dictionary entry
            gps_dict[image_name] = [latitude, longitude, altitude, roll, pitch, yaw]

        return gps_dict


def setExif(img_path, lat, lon, alt, roll, pitch, yaw):
    exif_dict = {'PSLatitudeRef': 'N',
                 'GPSLatitude': lat,
                 'GPSLongitudeRef': 'W',
                 'GPSLongitude': lon,
                 'GPSAltitudeRef': 0,
                 'GPSAltitude': alt,
                 'RelativeAltitude': alt,
                 'GimbalRollDegree': roll,
                 'GimbalPitchDegree': pitch,
                 'GimbalYawDegree': yaw}
    with ExifToolHelper(exifToolPath) as et:
        et.set_tags(img_path, exif_dict)


def update_Exif(jpeg_tuples, gps_dict):
    for jpeg_tuple in jpeg_tuples:
        image_name, image_path = jpeg_tuple[0], jpeg_tuple[1]
        if image_name in gps_dict:
            lat = gps_dict[image_name][0]
            lon = gps_dict[image_name][1]
            alt = gps_dict[image_name][2]
            roll = gps_dict[image_name][3]
            pitch = gps_dict[image_name][4]
            yaw = gps_dict[image_name][5]
            print(image_path, lat, lon, alt, roll, pitch, yaw)
            setExif(image_path, lat, lon, alt, roll, pitch, yaw)


jpg_folder = r'Y:\Superwake\Shoreline\BC_shoreline\01_geotagged_imagery\flight_08'
gps_csv = r'Y:\Superwake\Shoreline\BC_shoreline\03_bc_shoreline_working\gimble_data_merged.csv'


def overwrite_gps_exif_tags(jpg_folder, gps_csv):

    print('updating gps exif tags, number of images:')
    jpg_tuples = get_img_tuples(jpg_folder)
    print(len(jpg_tuples))
    gps_dict = get_gps_dict(gps_csv)
    update_Exif(jpg_tuples, gps_dict)

overwrite_gps_exif_tags(jpg_folder, gps_csv)
