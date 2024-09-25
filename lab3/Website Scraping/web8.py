from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

# Function to set up the Selenium WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service('C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe')  # Update with your path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Function to scrape product details from a given URL
def scrape_product_details(url):
    driver = setup_driver()
    driver.get(url)

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the product container
    products = soup.find_all('div', class_='item-box')

    product_list = []

    for product in products:
        title = product.find('a', class_='item-link').text.strip()
        price = product.find('strong').text.strip()
        old_price = product.find('span', class_='discount-price').text.strip() if product.find('span', class_='discount-price') else None
        discount = product.find('strong', class_='font-size12').text.strip() if product.find('strong', class_='font-size12') else None
        image_url = product.find('img')['data-src']
        
        product_list.append({
            'Title': title,
            'Price': price,
            'Old Price': old_price,
            'Discount': discount,
            'Image URL': image_url
        })

    driver.quit()
    return product_list

# Main execution
if __name__ == "__main__": 
    url = "https://www.hamzastore.pk/"
    products = scrape_product_details(url)

    # Convert to DataFrame for better visualization
    df = pd.DataFrame(products)

    # Save to CSV
    df.to_csv("hamzaStore.csv", index=False, encoding="utf-8")
   
