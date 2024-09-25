from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to your WebDriver (adjust the path accordingly)
webdriver_path = "C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe"  

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# URL of the website
url = 'https://bachydicar.com/'

# Open the website
driver.get(url)

# Allow the page to fully load
time.sleep(5)  # Adjust sleep time if necessary, based on page load speed

# Get the page source after loading
page_source = driver.page_source

# Close the WebDriver after getting the source
driver.quit()

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all product listings
products = soup.find_all('li', class_='wc-block-grid__product')

# Create lists to hold product details
product_names = []
prices_pk = []
prices_usd = []
product_links = []
image_urls = []

# Conversion rate from PKR to USD (adjust as needed)
conversion_rate = 270  # Example conversion rate

# Loop through each product and extract details
for product in products:
    title = product.find('div', class_='wc-block-grid__product-title').text.strip()
    price_text = product.find('div', class_='wc-block-grid__product-price').text.strip()
    
    # Extract numerical price value from the text
    try:
        price_pk = int(price_text.replace('₨', '').replace(',', '').split()[1])  # Extract the current price in PKR
    except (IndexError, ValueError):
        price_pk = 0  # Default value or handle the error as needed
   

    img_url = product.find('div', class_='wc-block-grid__product-image').img['src']
    product_url = product.find('a', class_='wc-block-grid__product-link')['href']
    
    # Append extracted details to the respective lists
    product_names.append(title)
    prices_pk.append(price_pk)
    product_links.append(product_url)
    image_urls.append(img_url)

# Create a DataFrame with the product details
df = pd.DataFrame({
    "Product Name": product_names,
    "Price (PKR)": prices_pk,
    "Product Link": product_links,
    "Image URL": image_urls
})

# Specify the CSV file name
csv_file = 'products.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False, encoding="utf-8")

print(f'Data has been written to {csv_file}')
