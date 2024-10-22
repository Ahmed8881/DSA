from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome driver
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store course details
titles = []
authors = []
ratings = []
descriptions = []
links = []

# Fetch webpage
driver.get("http://eduko.spikotech.com/Course")
time.sleep(5)  # Wait for the page to load completely
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract course details
for card in soup.find_all("div", class_="card-body text-center"):
    # Find course title
    title = card.find("h4", class_="card-title")
    
    # Find author
    author = card.find_all("h7")[0]
    
    # Find rating
    rating = card.find_all("h7")[1]
    
    # Find description
    description = card.find("p", class_="card-text")
    
    # Find link
    link = card.find("a", class_="btn")['href']
    
    if title and author and rating and description and link:
        # Append course details
        titles.append(title.get_text(strip=True))
        authors.append(author.get_text(strip=True))
        ratings.append(rating.get_text(strip=True))
        descriptions.append(description.get_text(strip=True))
        links.append("http://eduko.spikotech.com" + link)
    
    # Limit to 50 courses
    if len(titles) == 50:
        break

# Save to CSV
df = pd.DataFrame({
    "Title": titles,
    "Author": authors,
    "Rating": ratings,
    "Description": descriptions,
    "Link": links
})
df.to_csv("eduko-courses.csv", index=False, encoding="utf-8")

# Close the driver
driver.quit()

print("Data has been scraped and saved to eduko-courses.csv")