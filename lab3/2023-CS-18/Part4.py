from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
instructors = []
semesters = []

driver.get("http://eduko.spikotech.com")

time.sleep(5)

# Get the list of all course cards on the page
course_cards = driver.find_elements(By.XPATH, "//div[@class='card']")

for card in course_cards:
    # Scraping instructor name and semester from the course card
    instructor = card.find_element(By.XPATH, ".//h7[1]").text.strip()
    semester = card.find_element(By.XPATH, ".//h7[2]").text.strip()

    # Append instructor and semester to the lists
    instructors.append(instructor)
    semesters.append(semester)

    # Click the "Read More" link
    read_more_link = card.find_element(By.XPATH, ".//a[contains(text(), 'Read More')]")
    read_more_link.click()

    time.sleep(5)

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

    driver.back()

    # Adding sleep to allow the course list page to reload
    time.sleep(5)

# Create a DataFrame to save the data
df = pd.DataFrame({
    "Course Code": course_codes,
    "Course Name": course_names,
    "Course Description": course_descriptions,
    "CLOs": course_clos_list,
    "Books": course_books_list,
    "Instructor": instructors,
    "Semester": semesters
})

df.to_csv("Mydara.csv", index=False, encoding="utf-8")
driver.close()
