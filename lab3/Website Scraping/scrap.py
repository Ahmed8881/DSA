import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request to the URL
url = "http://eduko.spikotech.com/Course"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find the specific card containing the data
card = soup.find('div', class_='card-body text-center')

# Step 4: Extract the required data
title = card.find('h4', class_='card-title').text.strip()
author = card.find('h7').text.strip()
rating = card.find_all('h7')[1].text.strip()
description = card.find('p', class_='card-text').text.strip()
link = card.find('a', class_='btn')['href']

# Step 5: Create a DataFrame with the extracted data
data = {
    'Title': [title],
    'Author': [author],
    'Rating': [rating],
    'Description': [description],
    'Link': [link]
}
df = pd.DataFrame(data)

# Step 6: Save the DataFrame to a CSV file
df.to_csv('scraped_data.csv', index=False)

print("Data has been scraped and saved to scraped_data.csv")