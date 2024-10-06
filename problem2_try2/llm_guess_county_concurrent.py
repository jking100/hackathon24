import pandas as pd
from openai import  OpenAI
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set your OpenAI API key
client = OpenAI()

# Function to get the county from ChatGPT
def get_county_from_gpt(town, state):
    prompt = f"Answer only with the name of the county where the city of {town},{state} is located. Add nothing else. If you can't figure it out quickly, respond with NULL. Nothing else."
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=10  # Keep token usage low
    )
    
    # Extract and return the county name
    county_name = completion.choices[0].message.content.strip()
    # Use regular expression to remove 'county' and anything after, case insensitive
    cleaned_county_name = re.sub(r"\s*county.*", "", county_name, flags=re.IGNORECASE).strip()
    #print(cleaned_county_name)
    return cleaned_county_name

# Function to update a single row in the DataFrame
def update_row(row):
    town = row['Town']
    state = row['State/Province']
    #if pd.isna(row['County']) or row['County'] == '':
    county = get_county_from_gpt(town, state)
    return county


# Function to parallelize GPT requests and update the DataFrame
def parallel_update(df):
    with ThreadPoolExecutor(max_workers=10) as executor:  # Use 10 threads (adjust if needed)
        futures = {executor.submit(update_row, row): index for index, row in df.iterrows()}
        
        for future in as_completed(futures):
            index = futures[future]
            try:
                county = future.result()
                df.at[index, 'County'] = county
                if index % 100 == 0:
                    print(f"Processed {index} rows")
            except Exception as e:
                print(f"Error at row {index}: {e}")


# Read the CSV file
df = pd.read_csv("monarch_data/unique_town_state_us.csv")
# for testing
#df = pd.read_csv("monarch_data/top200.csv")

df['County'] = df['County'].astype(str)

# Call the function to parallelize the update
parallel_update(df)

# Save the updated DataFrame back to a new CSV
df.to_csv('monarch_data/updated_towns_with_counties.csv', index=False)

#df = pd.read_csv('monarch_data/updated_towns_with_counties.csv')

## should probably take a sample of 50 random rows not the header and then ask chatgpt if it looks good

# Sample 200 random rows from the CSV
SAMPLE_SIZE = 200
sampled_df = df.sample(n=SAMPLE_SIZE, random_state=42)

# Initialize a counter for wrong predictions
wrong_predictions = 0

# Define a function to query GPT-4 for a second opinion
def query_gpt_for_correctness(town, state, county):
    prompt = f"In which county is the town of {town} located in {state}? The current data suggests it is in {county}. Is this correct? Answer ONLY 'yes' or 'no' NOTHING ELSE."
    
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=10  # Keep token usage low
    )
    
    # Extract and return the county name
    answer = completion.choices[0].message.content.strip()
    if "no" in answer:
            return False  # Indicating that the model thinks it's wrong
    return True

# Loop through each row in the sample and query GPT-4
for index, row in sampled_df.iterrows():
    town = row['Town']
    state = row['State/Province']
    county = row['County']
    
    is_correct = query_gpt_for_correctness(town, state, county)
    
    if is_correct is False:
        wrong_predictions += 1

# Calculate the error rate
error_rate = (wrong_predictions / SAMPLE_SIZE) * 100
print(f"Error rate: {error_rate:.2f}%")
