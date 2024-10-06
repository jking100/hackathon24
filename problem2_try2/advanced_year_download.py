import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os

def download_data(year, season):
    base_url = "https://journeynorth.org/sightings/querylist.html"
    if season == "fall":
        url = f"{base_url}?season=fall&map=monarch-adult-fall&year={year}&submit=View+Data"
    else:
        url = f"{base_url}?season=spring&map=monarch-adult-spring&year={year}&submit=View+Data"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def main():
    '''
    if not os.path.exists('monarch_data'):
        os.makedirs('monarch_data')
    
    filename = f"monarch_data_all.csv"
    csvfile = open(f"monarch_data/{filename}", 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvfile)

    for year in range(1997, 2024):
        for season in ['spring', 'fall']:
            soup = download_data(year, season)
            
            table = soup.find('table')
            if table is None:
                print(f"No data found for {season} {year}")
                continue

            if(year==1997 and season=='spring'):
                headers = [th.text.strip() for th in table.find_all('th') if th.text.strip() != 'Image']
                writer.writerow(headers)

            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')
                row_data = [col.text.strip() for col in columns[:-1]]
                writer.writerow(row_data)

            print(f"Data for {season} {year} has been saved to '{filename}'")
    '''
    #f"monarch_data/{filename} contains all monarch data, now we filter down only to US data
    # List of valid US state abbreviations
    us_states = [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 
        'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 
        'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ]
    print(f"Filtering down the data to us only")

    # Read the CSV file
    df = pd.read_csv(f"monarch_data/monarch_data_all.csv")

    # Filter the DataFrame to keep only rows where the 'State/Province' is a valid US state abbreviation
    filtered_df = df[df['State/Province'].isin(us_states)]

    # Save the filtered data to a new CSV file
    filtered_df.to_csv(f"monarch_data/monarch_data_us.csv", index=False)

#now making the smaller unique town/state list with blank spot for county
    print("Making unique town/state .csv from US data")
    # Read the filtered CSV file
    df = pd.read_csv("monarch_data/monarch_data_us.csv")

    # Convert Town to lowercase (case insensitive) and State/Province to uppercase for uniformity
    df['Town'] = df['Town'].str.lower()
    df['State/Province'] = df['State/Province'].str.upper()

    # Create a new DataFrame with unique Town and State/Province combinations
    df_unique = df.drop_duplicates(subset=['Town', 'State/Province'], keep='first', 
                                ignore_index=True)

    # Add a blank 'County' column
    df_unique['County'] = ""

    # Select only the required columns
    df_final = df_unique[['Town', 'State/Province', 'County']]

    # Save the new DataFrame to a CSV file
    df_final.to_csv('monarch_data/unique_town_state_us.csv', index=False)



if __name__ == "__main__":
    main()