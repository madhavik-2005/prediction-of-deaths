import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

url = 'https://database.earth/population/india/deaths'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

# Initialize lists to store data
years = []
total_deaths = []
female_deaths = []
male_deaths = []

# Locate the table in the HTML
table = soup.find('table', class_='table-fixed w-full')

if table:
    # Find all rows in the table body
    rows = table.find('tbody').find_all('tr')

    for row in rows:
        # Extract all cells in the row
        cells = row.find_all('td')

        # Extract data for each column
        if len(cells) >= 4:  
            years.append(cells[0].text.strip())
            total_deaths.append(cells[1].text.strip())
            female_deaths.append(cells[2].text.strip())
            male_deaths.append(cells[3].text.strip())

    # Create a DataFrame
    deaths_data = pd.DataFrame({
        'Year': years,
        'Total Deaths': total_deaths,
        'Female Deaths': female_deaths,
        'Male Deaths': male_deaths
    })
    
    print(deaths_data)

    # Save data to Excel
    excel_file = 'Deaths.xlsx'
    deaths_data.to_excel(excel_file, index=False)

    print(f"Data has been saved to {excel_file}")
else:
    print("Table not found. The website structure might have changed.")
