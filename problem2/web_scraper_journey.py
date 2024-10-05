import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage
url = "https://journeynorth.org/sightings/querylist.html?season=fall&map=monarch-adult-fall&year=2023&submit=View+Data"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

# Open a CSV file to write the data
with open('monarch_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header, excluding the 'Image' column
    headers = [th.text.strip() for th in table.find_all('th') if th.text.strip() != 'Image']
    writer.writerow(headers)
    
    # Write the data rows, excluding the 'Image' column
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        row_data = [col.text.strip() for col in columns[:-1]]  # Exclude the last column (Image)
        writer.writerow(row_data)

print("Data has been successfully extracted and saved to 'monarch_data.csv'")