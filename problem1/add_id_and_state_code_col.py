import pandas as pd
import sys

# Check if the file path is provided
if len(sys.argv) < 2:
    print("Please provide the input CSV file path as an argument.")
    sys.exit(1)

# Get the input file path from the first command-line argument
input_file = sys.argv[1]

# Read the original CSV
df = pd.read_csv(input_file)

# Create the 'STATE' column by extracting the first two characters from 'Sample ID'
df['STATE'] = df['Sample ID'].str[:2]

# Create a 'MYID' column with unique integers (1 to n)
df['MYID'] = range(1, len(df) + 1)

# Rearrange columns
new_columns = ['MYID', 'STATE', 'Sample ID', 'Commod', 'Pesticide Code', 'Pesticide Name', 'Test Class', 
               'Concentration', 'LOD', 'pp_', 'Confirm 1', 'Confirm 2', 'Annotate', 'Quantitate', 
               'Mean', 'Extract', 'Determ', 'EPA Tolerance (ppm)']
df = df[new_columns]

# Write the modified DataFrame to a new CSV
output_file = "output.csv"
df.to_csv(output_file, index=False)

print(f"File saved as {output_file}")
