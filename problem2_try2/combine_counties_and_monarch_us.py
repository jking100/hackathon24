import pandas as pd

# Load CSV files
csv1_path = 'monarch_data/monarch_data_us.csv'
csv2_path = 'monarch_data/updated_towns_with_counties.csv'

csv1 = pd.read_csv(csv1_path)  # Load CSV1 (with Date, Town, State/Province, etc.)
csv2 = pd.read_csv(csv2_path)  # Load CSV2 (with Town, State/Province, County)

# Filter out rows in csv1 where State/Province is not a valid 2-character US state abbreviation
#valid_states = set(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
#                    'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 
#                    'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 
#                    'WI', 'WY'])

# Apply the filter to keep only rows with valid US state abbreviations
#csv1_filtered = csv1[csv1['State/Province'].apply(lambda x: isinstance(x, str) and x in valid_states)]

# Normalize case for Town and State columns in both csv1 and csv2 for case-insensitive matching
csv1['Town_lower'] = csv1['Town'].str.lower()
csv1['State_lower'] = csv1['State/Province'].str.lower()

csv2['Town_lower'] = csv2['Town'].str.lower()
csv2['State_lower'] = csv2['State/Province'].str.lower()

# Merge csv1 and csv2 based on Town and State/Province
merged_df = pd.merge(csv1, csv2[['Town_lower', 'State_lower', 'County']], how='left', 
                     left_on=['Town_lower', 'State_lower'], right_on=['Town_lower', 'State_lower'])

# Add the County from csv2 into csv1 and fill missing counties with 'NULL'
merged_df['County'] = merged_df['County'].fillna('NULL')

# Drop temporary lowercase columns
merged_df = merged_df.drop(columns=['Town_lower', 'State_lower'])

# Save the updated csv1 with the new County column
merged_df.to_csv('monarch_data/monarch_data_us_with_counties.csv', index=False)

print("Combined monarch_data_us.csv + updated_towns_with_counties.csv saved as 'monarch_data_us_with_counties.csv'")
