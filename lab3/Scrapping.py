from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep

service = Service(
    executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')

products = []  # List to store name of the product
prices = []  # List to store price of the product
# ratings = []  # List to store rating of the product

driver.get("https://www.hamzastore.pk/")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# print(soup)
for a in soup.findAll("div", attrs={"class": "deal-box"}):
    # print(a)
    # name = a.find("a", attrs={"class": "BiggerText"})
    name = a.find("p", attrs={"class": " roboto-700 "})
    price = a.find("span", attrs={"class": "PriceFont"})
    if name != None and price != None:
        products.append(name["title"])
        prices.append(price.text)
    if len(products) == 50:
        break

df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("item-box.csv", index=False, encoding="utf-8")


