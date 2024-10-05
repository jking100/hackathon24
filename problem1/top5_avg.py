import pandas as pd
import sys

# Check if the file path is provided
if len(sys.argv) < 2:
    print("Please provide the input CSV file path as an argument.")
    sys.exit(1)

# Get the input file path from the first command-line argument
input_file = sys.argv[1]

# Read the CSV with average concentrations
df = pd.read_csv(input_file)

# Sort values by 'STATE' and 'Average_Concentration' in descending order
df.sort_values(by=['STATE', 'Average_Concentration'], ascending=[True, False], inplace=True)

# Group by 'STATE' and keep the top 5 entries for each state
top5_df = df.groupby('STATE').head(5)

# Write the resulting DataFrame to a new CSV
output_file = "top5_average_concentration_output.csv"
top5_df.to_csv(output_file, index=False)

print(f"Top 5 average concentration file saved as {output_file}")
