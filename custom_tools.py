import os
import pandas as pd
import re


# Specify the folder path where your CSV files are located

def merge_all_gimble_csv(folder_path: str, out_csv_name: str):
    # Initialize an empty DataFrame to store the merged data
    master_df = pd.DataFrame()

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            base_name, extension = os.path.splitext(filename)

            # Check if the file has a corresponding capture_time file
            capture_time_file = f"{base_name}_capture_time.csv"
            if capture_time_file in os.listdir(folder_path):
                # Extract flight information using regular expressions
                match = re.match(r'Flight_(\d+)_(\d+)_(\d+)', base_name)
                if match:
                    flight_number, flight_date, flight_time = match.groups()

                    # Read both CSV files into pandas DataFrames
                    base_df = pd.read_csv(os.path.join(folder_path, filename))
                    capture_time_df = pd.read_csv(os.path.join(folder_path, capture_time_file))

                    # Merge the two DataFrames on different common columns
                    merged_df = pd.merge(base_df, capture_time_df[['#[filename]', '[capture time ms]']],
                                         left_on='# image name', right_on='#[filename]')
                    merged_df['flight_number'] = flight_number
                    merged_df['flight_date'] = flight_date
                    merged_df['flight_time'] = flight_time
                    # Append the merged DataFrame to the master DataFrame
                    master_df = pd.concat([master_df, merged_df])

    print("Merging and appending completed.")

    # Save the master DataFrame to a new CSV file
    master_df.to_csv(os.path.join(folder_path, out_csv_name + '.csv'), index=False)

    print("CSV file created: " + out_csv_name + '.csv')
    return master_df
