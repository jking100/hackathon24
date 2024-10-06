import requests
from bs4 import BeautifulSoup
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
    if not os.path.exists('monarch_data'):
        os.makedirs('monarch_data')
    
    #os.chdir('monarch_data')

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

if __name__ == "__main__":
    main()