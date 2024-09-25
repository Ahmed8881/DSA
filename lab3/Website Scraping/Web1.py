from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time
# Setup Chrome driver
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store product details
products = []
prices = []
discounts = []
ratings = []
image_urls = []

# Fetch webpage
driver.get("https://www.daraz.pk/")
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract product details
for a in soup.find_all("a", class_="pc-custom-link jfy-item hp-mod-card-hover"):
    # Find product name
    name = a.find("div", class_="card-jfy-title")
    
    # Find price
    price = a.find("span", class_="price")
    
    # Find discount (optional, if available)
    discount = a.find("span", class_="hp-mod-discount")
    
    # Find rating (if available)
    rating = a.find("div", class_="card-jfy-rating-layer top-layer checked")
    
    # Find image URL
    image = a.find("img")
    
    if name and price and image:
        # Append product details
        products.append(name.get_text(strip=True))
        prices.append(price.get_text(strip=True))
        
        # Append discount if available
        discounts.append(discount.get_text(strip=True) if discount else "No discount")
        
        # Append rating if available
        ratings.append(rating['style'].replace('width: ', '').replace('%;', '') if rating else "No rating")
        
        # Append image URL
        image_urls.append(image['src'])
    
    # Limit to 50 products
    if len(products) == 50:
        break

# Save to CSV
df = pd.DataFrame({
    "Product Name": products,
    "Price": prices,
    "Discount": discounts,
    "Rating (%)": ratings,
    "Image URL": image_urls
})
df.to_csv("daraz-products.csv", index=False, encoding="utf-8")

# Close the driver
driver.quit()
