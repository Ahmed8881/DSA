from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time  # Import time for delays
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setting up the ChromeDriver service
service = Service(executable_path="C:/Users/butta/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Lists to store scraped data
course_codes = []
course_names = []
course_descriptions = []
course_clos_list = []
course_books_list = []

# Opening the webpage
driver.get("http://eduko.spikotech.com")

# Adding sleep to allow the page to fully load
time.sleep(5)

# Get the list of all "Read More" links on the page
read_more_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Read More')]")

# Loop through all courses and scrape details
for link in read_more_links:
    try:
        # Click the "Read More" link
        link.click()

        # Adding sleep to allow the course details page to load
        time.sleep(5)

        # Get the page source of the course details page
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        # Scraping the course code
        course_code = soup.find("div", id="CourseCode").text.strip()

        # Scraping the course name
        course_name = soup.find("h5", id="CourseName").text.strip()

        # Scraping the course description
        course_description = soup.find("p", id="CourseDescription").text.strip()

        # Scraping the course learning outcomes (CLOs)
        course_clos = soup.find("ul", id="CourseClos").find_all("li")
        course_clos_text = ", ".join([clo.text.strip() for clo in course_clos])

        # Scraping the textbooks
        course_books = soup.find("ul", id="CourseBooks").find_all("li")
        course_books_text = ", ".join([book.text.strip() for book in course_books])

        # Append the scraped data to lists
        course_codes.append(course_code)
        course_names.append(course_name)
        course_descriptions.append(course_description)
        course_clos_list.append(course_clos_text)
        course_books_list.append(course_books_text)

        # Go back to the previous page (course list)
        driver.back()

        # Adding sleep to allow the course list page to reload
        time.sleep(5)

        # Re-fetch the "Read More" links after going back
        read_more_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Read More')]")

    except Exception as e:
        print(f"Error scraping course: {e}")
        driver.back()
        time.sleep(5)
        read_more_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Read More')]")

# Create a DataFrame to save the data
df = pd.DataFrame({
    "Course Code": course_codes,
    "Course Name": course_names,
    "Course Description": course_descriptions,
    "CLOs": course_clos_list,
    "Books": course_books_list
})

# Save the DataFrame to a CSV file
df.to_csv("all-course-details.csv", index=False, encoding="utf-8")

# Closing the driver after scraping
driver.close()
