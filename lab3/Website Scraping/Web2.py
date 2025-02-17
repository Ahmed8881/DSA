import time  # Add this import to handle delay
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service

# Setup Chrome driver
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Fetch webpage
driver.get("https://www.whatmobile.com.pk/")  # Replace with actual URL

# Wait for the page to load completely (adjust the sleep time if needed)
time.sleep(5)  # 5 seconds delay

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Now you can close the browser after the page source is fetched
driver.quit()

# Lists to store product details
products = []
prices = []
usd_prices = []
product_links = []
image_urls = []

# Extract product details
for li in soup.find_all("li", class_="product"):
    # Find product name
    name_tag = li.find("h4", class_="p4 biggertext")
    name = name_tag.get_text(strip=True).replace("\n", " ")
    
    # Find price in PKR
    price = li.find("span", class_="PriceFont").get_text(strip=True)
    
    # Find USD price from title attribute in the <a> tag
    usd_price = li.find("a")["title"].replace("Price USD ", "")
    
    # Find product link
    link = li.find("a")["href"]
    
    # Find image URL
    image_url = li.find("img")["src"]
    
    # Append product details
    products.append(name)
    prices.append(price)
    usd_prices.append(usd_price)
    product_links.append(link)
    image_urls.append(image_url)

# Save to CSV
df = pd.DataFrame({
    "Product Name": products,
    "Price (PKR)": prices,
    "Price (USD)": usd_prices,
    "Product Link": product_links,
    "Image URL": image_urls
})
df.to_csv("mobile-phones.csv", index=False, encoding="utf-8")
