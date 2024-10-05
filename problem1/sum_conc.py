import pandas as pd
import sys

# Check if the file path is provided
if len(sys.argv) < 2:
    print("Please provide the input CSV file path as an argument.")
    sys.exit(1)

# Get the input file path from the first command-line argument
input_file = sys.argv[1]

# Read the modified CSV
df = pd.read_csv(input_file)

# Group by 'STATE', 'Pesticide Code', and 'Pesticide Name' and calculate total concentration
summary_df = df.groupby(['STATE', 'Pesticide Code', 'Pesticide Name'], as_index=False)['Concentration'].sum()

# Rename the 'Concentration' column to 'Total_Concentration'
summary_df.rename(columns={'Concentration': 'Total_Concentration'}, inplace=True)

# Reorder the columns
summary_df = summary_df[['STATE', 'Pesticide Code', 'Pesticide Name', 'Total_Concentration']]

# Write the summarized DataFrame to a new CSV
output_file = "summary_output.csv"
summary_df.to_csv(output_file, index=False)

print(f"Summary file saved as {output_file}")
