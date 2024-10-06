import csv
from collections import defaultdict

# List of US state abbreviations
US_STATES = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
}

def process_csv(input_file, output_file):
    unique_combinations = defaultdict(set)
    
    # Read the input CSV and collect unique town-state combinations
    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            town = row['Town'].strip().lower()
            state = row['State/Province'].strip().upper()
            if state in US_STATES:
                unique_combinations[state].add(town)
    
    # Write the unique combinations to the output CSV
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Town', 'State', 'County'])  # Write header
        
        for state, towns in unique_combinations.items():
            for town in towns:
                writer.writerow([town.title(), state, ''])  # Leave County blank

# Usage
input_file = 'monarch_data/monarch_data_all.csv'
output_file = 'monarch_data/unique_towns_us.csv'
process_csv(input_file, output_file)