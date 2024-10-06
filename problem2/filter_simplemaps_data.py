import pandas as pd

# Load the CSV file
input_file = "uscities.csv"  # Replace with the name of your input CSV
output_file = "monarch_data/county_data.csv"  # This will be your output file

# Columns to keep
columns_to_keep = ['city_ascii', 'state_id', 'county_name', 'lat', 'lng']

# Load the CSV, keeping only the specified columns
df = pd.read_csv(input_file, usecols=columns_to_keep)

# Save the filtered data to a new CSV file
df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
