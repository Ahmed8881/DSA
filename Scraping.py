from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome( service=Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe"), options=options)

    # Open the URL using Selenium
    driver.get(url)

    # Wait for the page to load
    time.sleep(3)

    # Get the page source (HTML)
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    # Extract all text from the page
    page_text = soup.get_text()

    # Optionally, if you want to extract all the HTML elements, you can do that too:
    page_html = soup.prettify()

    # Return the text and HTML content
    return page_text, page_html

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    text, html = scrape_website(url)

    # Save the extracted text and HTML to files (optional)
    with open("scraped_text.txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)

    with open("scraped_html.html", "w", encoding="utf-8") as html_file:
        html_file.write(html)

    print("Scraping complete! Check the 'scraped_text.txt' and 'scraped_html.html' files.")
