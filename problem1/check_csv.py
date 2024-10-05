import pandas as pd
import sys

# Load the CSV file into a DataFrame
def check_blank_rows_columns(file_path):
    df = pd.read_csv(file_path)

    # Check for entirely blank rows
    blank_rows = df.isnull().all(axis=1)
    if blank_rows.any():
        print(f"Blank rows found at indices: {df.index[blank_rows].tolist()}")
    else:
        print("No entirely blank rows found.")

    # Check for entirely blank columns
    blank_columns = df.isnull().all(axis=0)
    if blank_columns.any():
        print(f"Blank columns found: {df.columns[blank_columns].tolist()}")
    else:
        print("No entirely blank columns found.")

# Ensure a file path is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

# Get the file path from the first command-line argument
file_path = sys.argv[1]
check_blank_rows_columns(file_path)
