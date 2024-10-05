import pandas as pd
import sys

# Check if the file path is provided
if len(sys.argv) < 2:
    print("Please provide the input CSV file path as an argument.")
    sys.exit(1)

# Get the input file path from the first command-line argument
input_file = sys.argv[1]

# Read the modified CSV
df = pd.read_csv(input_file, low_memory=False)

# Group by 'STATE' column and count occurrences of each state
state_counts = df['STATE'].value_counts()

# Print distinct states and their counts
for state, count in state_counts.items():
    print(f"State: {state}, Count: {count}")
