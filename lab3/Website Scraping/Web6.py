from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

gamingDesktops = {
    "Name": [],
    "Price": [],
    "Sold": [],
    "FreeShipping": [],
    "StoreName": [],
    "Link": []
}

driver = webdriver.Chrome()
driver.get("https://www.aliexpress.com/w/wholesale-Desktops.html?isFromCategory=y&categoryUrlParams=%7B%22q%22%3A%22Desktops%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22category_navigate%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22b3269b84-0b88-4bd8-ab28-7c3cf27ff97d%22%2C%22scene_id%22%3A%2237749%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22en%22%2C%22bizScene%22%3A%22category_navigate%22%2C%22guideModule%22%3A%22category_navigate_vertical%22%2C%22postCatIds%22%3A%227%2C21%22%2C%22scene%22%3A%22category_navigate%22%7D&g=n&SearchText=Desktops")
sleep(5)

for i in range(10):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for item in soup.find_all("div", class_="manhattan--container--1lP57Ag cards--gallery--2o6yJVt"):
        name = item.find("h3", class_="manhattan--titleText--WccSjUS").text
        sold = item.find("span", class_="manhattan--trade--2PeJIEB")
        sold = sold.text if sold else "0 sold"
        freeshipping = True if item.find("span", class_="tag--text--1BSEXVh tag--textStyle--3dc7wLU manhattan--serviceStyle--1Z6RxQ4") else False
        storeName = item.find("a", class_="store--name--2Jk7x5").text
        link = item.find("a", class_="manhattan--container--1lP57Ag")["href"]
        price = ""
        for span in item.find("div", class_="manhattan--price-sale--1CCSZfK").find_all("span"):
            price += span.text
        for key, value in zip(gamingDesktops.keys(), [name, price, sold, freeshipping, storeName, link]):
            gamingDesktops[key].append(value)
    try:
        driver.find_element(By.CLASS_NAME, "comet-pagination-item-link").click()
    except Exception as e:
        print(f"Error clicking pagination: {e}")
        break
    sleep(5)
driver.quit()
# Print the data

df = pd.DataFrame(gamingDesktops)
print(df)
df.to_csv("gamingDesktopsAliExpress.csv", index=False)
 