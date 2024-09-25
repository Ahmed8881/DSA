import time 
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service

# Setup Chrome driver
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Fetch webpage
driver.get("https://homeshopping.pk/")  # The actual URL to scrape

# Wait for the page to load completely (adjust the sleep time if needed)
time.sleep(5)  # 5 seconds delay

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Now you can close the browser after the page source is fetched
driver.quit()

# Lists to store product details
products = []
prices = []
product_links = []
image_urls = []

# Extract product details
for item in soup.find_all("div", class_="product-box"):
    # Find product name
    name_tag = item.find("h5", class_="ProductDetails")
    name = name_tag.get_text(strip=True) if name_tag else "N/A"
    
    # Find price in PKR
    price_tag = item.find("div", class_="ActualPrice")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"
    
    # Find product link
    link_tag = item.find("a", href=True)
    link = link_tag["href"] if link_tag else "N/A"
    
    # Find image URL
    img_tag = item.find("img", class_="img-responsive")
    image_url = img_tag.get("data-src") or img_tag.get("src") if img_tag else "N/A"
    
    # Append product details
    products.append(name)
    prices.append(price)
    product_links.append(link)
    image_urls.append(image_url)

# Save to CSV
df = pd.DataFrame({
    "Product Name": products,
    "Price (PKR)": prices,
    "Product Link": product_links,
    "Image URL": image_urls
})
df.to_csv("onlineshop.csv", index=False, encoding="utf-8")
