# Python Web Scraping

**Web scraping** is the process of extracting and collecting data from websites automatically using code.

---

## Prerequisites

### Required Libraries

Install both libraries using pip before getting started:

```bash
pip install requests
pip install beautifulsoup4
```

| Library | Purpose |
|---------|---------|
| `requests` | Sends HTTP requests to fetch website content |
| `beautifulsoup4` | Parses and navigates HTML content |

### Required Knowledge

Basic understanding of **HTML tags** and **CSS selectors** is needed. Content is targeted using:

- HTML tags (e.g. `<h1>`, `<p>`, `<div>`)
- Class names (e.g. `class="title"`)
- IDs (e.g. `id="main-content"`)

---

## 1. Importing Libraries

```python
import requests
from bs4 import BeautifulSoup
import json
```

---

## 2. Fetching a Web Page

Use `requests.get()` to send an HTTP GET request to the target URL and retrieve the page content.

```python
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

# get all the content from the website
content = response.content

# check the status code
status = response.status_code
print(status)  # 200 means success
```

### Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| `200` | OK — request was successful |
| `404` | Not Found — page does not exist |
| `403` | Forbidden — access is denied |
| `500` | Internal Server Error |

---

## 3. Parsing HTML with BeautifulSoup

Pass the raw content to `BeautifulSoup` along with a parser. `html.parser` is Python's built-in HTML parser and requires no extra installation.

```python
soup = BeautifulSoup(content, 'html.parser')
```

---

## 4. Navigating the Parsed Content

Once parsed, you can access different parts of the HTML using tag names.

```python
print(soup.title)           # full <title> tag and content
print(soup.title.get_text()) # just the text inside <title>
print(soup.body)             # full <body> content
```

### Useful BeautifulSoup Methods

| Method | Description |
|--------|-------------|
| `soup.title` | Access the `<title>` tag |
| `soup.body` | Access the `<body>` tag |
| `.get_text()` | Extract only the text, stripping all HTML tags |
| `soup.find("tag")` | Find the first occurrence of a tag |
| `soup.find_all("tag")` | Find all occurrences of a tag |

---

## 5. Saving Scraped Data to a JSON File

After scraping, the data can be structured and saved to a `.json` file for later use or analysis.

```python
if soup.body:
    json_data = {
        "html": str(soup.body),       # raw HTML as a string
        "text": soup.body.get_text(), # plain text content
        "status_code": status         # HTTP status code
    }

    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    print("JSON file created: scraped_data.json")
```

### `json.dump()` Parameters

| Parameter | Description |
|-----------|-------------|
| `indent=4` | Pretty-prints the JSON with 4-space indentation |
| `ensure_ascii=False` | Allows non-ASCII characters (e.g. accented letters) to be saved correctly |

---

## Full Code

```python
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

content = response.content
status = response.status_code

soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(status)

if soup.body:
    json_data = {
        "html": str(soup.body),
        "text": soup.body.get_text(),
        "status_code": status
    }

    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    print("JSON file created: scraped_data.json")
```

---

## Web Scraping Workflow

```
1. Identify the target URL
        ↓
2. Send a GET request with requests.get()
        ↓
3. Check the status code (200 = success)
        ↓
4. Parse the HTML content with BeautifulSoup
        ↓
5. Navigate and extract the data you need
        ↓
6. Save or process the extracted data
```

> **Tip:** Always check a website's `robots.txt` file (e.g. `https://example.com/robots.txt`) and terms of service before scraping to ensure you are allowed to do so.
