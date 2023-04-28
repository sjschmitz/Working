##########
#Query start/end dates for USGS gages from nwis server and write to streamflow catalog
#last update: 4.27.2023
#
#processes:
#   query site data from nwis
#   parse start/end dates
#   import catalog
#   write nwis objects into excel
#   FACT CHECK!!
##########




import requests
import dataretrieval as nwis
import pandas as pd
import openpyxl as py
import numpy as np

# Define file path, on local
file_path = 'C:/Users/sjsch/Desktop/Streamflow/USGS_updated.xlsx'
print('Import success')


#query nwis server and define specific objects of interest
def get_measurement_dates(gage_number):
    url = f"https://waterservices.usgs.gov/nwis/site/?format=json&sites={gage_number}"
    response = requests.get(url)

    try:
        response.raise_for_status()  # Check for any HTTP errors
        site_info = response.json()

        site_data = site_info['sites'][0]
        parameter_group = site_data['parameterGroup']
        parameter_group_info = next((group for group in parameter_group if group['name'] == 'Information'), None)

        oldest_measurement = parameter_group_info['beginDate']
        most_recent_measurement = parameter_group_info['endDate']

        measurement_dates = {'oldest_measurement': oldest_measurement, 'most_recent_measurement': most_recent_measurement}

        return measurement_dates

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.JSONDecodeError as e:
        print("JSON Decode Error:", e)

    return None

# Example usage
gage_number = '11493500'
measurement_dates = get_measurement_dates(gage_number)

if measurement_dates is not None:
    print("Oldest measurement date:", measurement_dates['oldest_measurement'])
    print("Most recent measurement date:", measurement_dates['most_recent_measurement'])

start_date_column = 'start_date'  # Replace with start date column name
end_date_column = 'end_date'  # Replace with end date column name

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Iterate through the rows and find matching IDs
for index, row in df.iterrows():
    if row['ID'] == target_id:  # Replace 'ID' with actual column name
        df.at[index, start_date_column] = '2023-01-01'  # Replace with start date
        df.at[index, end_date_column] = '2023-12-31'  # Replace with end date

# Save the modified DataFrame back to the Excel file
df.to_excel(file_path, index=False)
print("values written")
print('saved')

