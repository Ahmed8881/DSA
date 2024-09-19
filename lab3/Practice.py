# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df.dtypes)
# list1=df['Name'].values.tolist()
# list2=df['Age'].values.tolist()
# plt.bar(list1,list2)
# plt.show()
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep

# webdriver can be downloaded from
# https://sites.google.com/chromium.org/driver/downloads/versionselection?authuser=0

service = Service(
    executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')

products = []  # List to store name of the product
prices = []  # List to store price of the product
# ratings = []  # List to store rating of the product

driver.get("https://www.whatmobile.com.pk/")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# print(soup)
for a in soup.findAll("div", attrs={"class": "quick-buttons "}):
    print(a)
    name = a.find("a", attrs={"class": "BiggerText"})
    price = a.find("span", attrs={"class": "PriceFont"})
    if name != None and price != None:
        products.append(name["title"])
        prices.append(price.text)
    if len(products) == 50:
        break

df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("product.csv", index=False, encoding="utf-8")
