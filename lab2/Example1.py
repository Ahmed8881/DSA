import csv
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Initialize Selenium WebDriver (using Chrome in this example)
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no browser UI)
    driver = webdriver.Chrome(options=options)
    return driver

# Check if an element has no children (i.e., it's a leaf node)
def is_leaf_node(element):
    return not element.findChildren()

# Function to scrape data from a given URL
def scrape_data(url):
    driver = get_driver()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()  # Close the Selenium browser

    # Dictionary to store scraped data by class name
    scraped_data = {}

    # Find all elements with a class attribute that contains the word 'container'
    containers = soup.find_all(class_=lambda class_name: class_name and 'container' in class_name)
    for container in containers:
        # Find all elements with a class attribute that have no child elements (leaf nodes) within the container
        for element in container.find_all(class_=True):
            if is_leaf_node(element):
                class_name = ' '.join(element['class'])  # Get class name(s)
                text = element.get_text(strip=True)      # Get text content

                # Append data to the corresponding class in the dictionary
                if class_name not in scraped_data:
                    scraped_data[class_name] = [text]
                else:
                    scraped_data[class_name].append(text)

    return scraped_data

# Save scraped data to a CSV file
def save_to_csv(data, output_filename='scraped_data.csv'):
    # Filter out empty values
    filtered_data = {k: [v for v in values if v] for k, values in data.items()}

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in filtered_data.items()]))

    # Save DataFrame to CSV
    df.to_csv(output_filename, index=False)

# Main function to scrape and save
def scrape_and_save(url):
    print(f"Scraping data from {url}")
    scraped_data = scrape_data(url)
    
    # Check if data was found
    if scraped_data:
        output_filename = f"{os.path.basename(url)}_scraped.csv"
        save_to_csv(scraped_data, output_filename)
        print(f"Data saved to {output_filename}")
    else:
        print("No data found.")

# Example usage
if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scrape_and_save(url)