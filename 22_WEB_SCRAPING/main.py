# Web scraping is the process of extracting and collecting data from websites

# to start scraping websites you need requests, beautifulSoup4 and a website.

# to scrape data from websites basic understanding of HTML tags and css selectors is needed. we target content from a website using HTML tags, classes or/and ids


# pip install requests and pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)

# get all the content from the website
content = response.content

# parse the content using beautiful soup and specify the parser to be used
soup = BeautifulSoup(content, 'html.parser')

print(soup.title)

print(soup.title.get_text())

print(soup.body)
status = response.status_code
print(status)

# Convert soup.body to JSON file
if soup.body:
    json_data = {
        "html": str(soup.body),
        "text": soup.body.get_text(),
        "status_code": status
    }
    
    # Save to separate JSON file in this folder
    with open(r'e:\python tutorial\DAY_22_WEB_SCRAPING\scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    
    print("JSON file created: scraped_data.json")

