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
driver.get("https://www.dvago.pk/")  # Replace with the actual URL

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
for li in soup.find_all("li", class_="ProductCard_productListWrapper__WyYAq"):
    # Find product name
    name_tag = li.find("p", class_="MuiTypography-root MuiTypography-body1 css-9l3uo3")
    name = name_tag.get_text(strip=True).replace("\n", " ") if name_tag else "N/A"
    
    # Find price
    price_tag = li.find("p", class_="ProductCard_salePrice___b0BY css-9l3uo3")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"
    
    # Find product link
    link_tag = li.find("a")
    link = link_tag["href"] if link_tag else "N/A"
    
    # Complete link with base URL
    full_link = f"https://www.dvago.pk{link}" if link != "N/A" else "N/A"
    
    # Find image URL
    img_tag = li.find("img")
    image_url = img_tag["src"] if img_tag else "N/A"
    
    # Append product details
    products.append(name)
    prices.append(price)
    product_links.append(full_link)
    image_urls.append(image_url)

# Save to CSV
df = pd.DataFrame({
    "Product Name": products,
    "Price (PKR)": prices,
    "Product Link": product_links,
    "Image URL": image_urls
})
df.to_csv("dvago-web.csv", index=False, encoding="utf-8")
