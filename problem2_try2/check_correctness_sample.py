import pandas as pd
from openai import  OpenAI

client = OpenAI()

df = pd.read_csv('monarch_data/monarch_data_us_with_counties.csv')

## should probably take a sample of some random rows not the header and then ask chatgpt if it looks good

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