import custom_tools

# Specify the folder path where gimble CSV files are located
gimble_csv_folder = r'Y:\Superwake\Shoreline\BC_shoreline\01_imagery_trasfer_20240107\geotag_log'
out_gimble_file = r'Y:\Superwake\Shoreline\BC_shoreline\03_bc_shoreline_working\gimble_data_merged.csv'
# run all
gimble_df = custom_tools.merge_all_gimble_csvs(gimble_csv_folder, 'merged_gimble_data')
gimble_df_with_utm = custom_tools.apply_utm_conversion(gimble_df)
# Save the master DataFrame to a new CSV file

gimble_df_with_utm.to_csv(out_gimble_file)
