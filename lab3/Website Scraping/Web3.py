import time  # Add this import to handle delay
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service

# Setup Chrome driver
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=options)

# Fetch webpage
driver.get("https://www.amazon.com/s?k=women+watch")  # Replace with actual URL

# Wait for the page to load completely (adjust the sleep time if needed)
time.sleep(5)  # 5 seconds delay

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Now you can close the browser after the page source is fetched
driver.quit()

# Lists to store product details
products = []
ratings = []
prices = []
product_links = []
image_urls = []

# Extract product details
for div in soup.find_all("div", {"data-component-type": "s-search-result"}):
    # Find product name
    name_tag = div.find("h2", class_="a-size-mini")
    if name_tag:
        name = name_tag.get_text(strip=True)
        
        # Find rating
        rating_tag = div.find("span", class_="a-declarative")
        rating = rating_tag["aria-label"] if rating_tag and rating_tag.has_attr("aria-label") else "No rating"
        
        # Find price
        price_tag = div.find("span", class_="a-price-whole")
        if price_tag:
            price = price_tag.get_text(strip=True)
        else:
            price = "Price not available"
        
        # Find product link
        link_tag = div.find("a", class_="a-link-normal")
        link = "https://www.amazon.com" + link_tag["href"] if link_tag else "Link not available"
        
        # Find image URL
        image_tag = div.find("img", class_="s-image")
        image_url = image_tag["src"] if image_tag else "Image not available"
        
        # Append product details
        products.append(name)
        ratings.append(rating)
        prices.append(price)
        product_links.append(link)
        image_urls.append(image_url)

# Save to CSV
df = pd.DataFrame({
    "Product Name": products,
    "Rating": ratings,
    "Price": prices,
    "Product Link": product_links,
    "Image URL": image_urls
})
df.to_csv("women-watches.csv", index=False, encoding="utf-8")
