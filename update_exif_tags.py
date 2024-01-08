import custom_tools


# Specify the folder path where gimble CSV files are located
gimble_csv_folder = r'Y:\Superwake\Shoreline\BC_shoreline\01_imagery_trasfer_20240107\geotag_log'

# run all
gimble_df = custom_tools.merge_all_gimble_csv(gimble_csv_folder, 'merged_gimble_data')
