import pandas as pd
import sys

# Check if a filename was provided
if len(sys.argv) < 2:
    print("Usage: python filter_pesticides.py <filename>")
    sys.exit(1)

# Get the filename from command-line arguments
filename = sys.argv[1]

# Load the CSV file
df = pd.read_csv(filename)

# Group by 'STATE' and find the row with the maximum 'Average_Concentration'
result = df.loc[df.groupby('STATE')['Average_Concentration'].idxmax()]

# Save the result to a new CSV file (optional)
result.to_csv('filtered_file.csv', index=False)
