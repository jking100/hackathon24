import pandas as pd
import sys

# Load the CSV file and print data types of columns
def inspect_column_data_types(file_path):
    df = pd.read_csv(file_path)
    
    # Print the general data types for each column
    print("Data Types of Columns:")
    print(df.dtypes)
    print("\n")

    # For any column with mixed types, display the types of values it contains
    # Checking 'object' type columns, which could have mixed data types
    for col in df.columns:
        if df[col].dtype == 'object':
            unique_types = df[col].apply(type).unique()
            print(f"Column '{col}' contains the following data types: {unique_types}")
        else:
            print(f"Column '{col}' is of uniform type: {df[col].dtype}")
            
# Ensure a file path is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

# Get the file path from the first command-line argument
file_path = sys.argv[1]
inspect_column_data_types(file_path)
