import pandas as pd

# Load both CSV files
csv1 = pd.read_csv('monarch_data/unique_towns_us.csv')  # Your first file (Town,State,County)
csv2 = pd.read_csv('monarch_data/county_data.csv')  # Your second file (city_ascii,state_id,county_name,lat,lng)

# Normalize the city and state columns to lowercase for case-insensitive matching
csv1['Town_lower'] = csv1['Town'].str.lower()
csv1['State_lower'] = csv1['State'].str.lower()

csv2['city_ascii_lower'] = csv2['city_ascii'].str.lower()
csv2['state_id_lower'] = csv2['state_id'].str.lower()

# Merge csv1 with csv2 based on the lowercased city and state values
merged_df = pd.merge(csv1, csv2, how='left', left_on=['Town_lower', 'State_lower'], right_on=['city_ascii_lower', 'state_id_lower'])

# Fill in the County in csv1 with the matched county from csv2, or NULL if no match
csv1['County'] = merged_df['county_name'].fillna('NULL')

# Drop the temporary lowercase columns
csv1 = csv1.drop(columns=['Town_lower', 'State_lower'])

# Save the updated csv1 with county information
csv1.to_csv('monarch_data/updated_unique_towns_us_with_counties.csv', index=False)

print("Updated unique_towns_us.csv saved as 'updated_unique_towns_us_with_counties.csv'")
