from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service

# Setup Chrome driver
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store product details
products = []
prices = []

# Fetch webpage
driver.get("https://www.hamzastore.pk/")
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract product details
for a in soup.find_all("div", class_="deal-box"):
    name = a.find("p", class_=" roboto-700 ")
    price = a.find("span", class_="PriceFont")
    if name and price:
        products.append(name.get_text(strip=True))
        prices.append(price.get_text(strip=True))
    if len(products) == 50:
        break

# Save to CSV
df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("item-box.csv", index=False, encoding="utf-8")

# Close the driver
driver.quit()
