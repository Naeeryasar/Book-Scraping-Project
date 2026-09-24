# Book Scraping Project

A simple Python web-scraping project that collects book information from [Books to Scrape](https://books.toscrape.com/) and saves the results into a CSV file.

The project demonstrates how to use **Requests**, **BeautifulSoup**, and **Pandas** to scrape structured data from web pages.

## Features

* Scrapes multiple pages of books
* Collects book titles
* Collects book prices
* Collects book ratings
* Uses `requests` to download web pages
* Uses `BeautifulSoup` to parse HTML
* Uses `Pandas` to organize and export data
* Saves the scraped data as a CSV file

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* Pandas

## Project Structure

```text
Book-Scraping-Project/
├── main.py
└── README.md
```

After running the program, a CSV file is also generated:

```text
Book_info.csv
```

## Requirements

Python 3.8 or newer is recommended.

Install the required packages:

```bash
pip install requests beautifulsoup4 pandas
```

On some systems:

```bash
pip3 install requests beautifulsoup4 pandas
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Naeeryasar/Book-Scraping-Project.git
cd Book-Scraping-Project
```

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

## Run the Project

Run:

```bash
python main.py
```

The program accesses the Books to Scrape website and processes the configured catalog pages.

During execution, it displays messages such as:

```text
Scrapping Page 1
Scrapping Page 2
Scrapping Page 3
Scrapping Page 4
```

After scraping, it reports the total number of books collected.

## Data Collected

The project stores the following information:

| Field  | Description       |
| ------ | ----------------- |
| Title  | Title of the book |
| Price  | Listed book price |
| Rating | Star rating       |

The resulting data is saved to:

```text
Book_info.csv
```

## Example CSV

The output CSV has the following structure:

```csv
Title,Price,Rating
A Light in the Attic,£51.77,Three
Tipping the Velvet,£53.74,One
Soumission,£50.10,One
```

The actual values depend on the content returned by the website when the scraper runs.

## How It Works

### 1. Send HTTP Request

The script uses the `requests` library to download each catalog page:

```python
response = requests.get(url, headers=header)
```

A browser-style User-Agent is supplied in the request headers.

### 2. Parse HTML

BeautifulSoup is used to parse the downloaded page:

```python
soup = BeautifulSoup(response.text, "html.parser")
```

### 3. Find Books

Books are identified using the site's product article structure:

```python
books = soup.find_all("article", class_="product_pod")
```

### 4. Extract Information

For each book, the script extracts:

* Title
* Price
* Rating

### 5. Save to CSV

Pandas converts the collected data into a DataFrame and exports it:

```python
df.to_csv("Book_info.csv", index=False)
```

## Target Website

This project uses:

**Books to Scrape**

https://books.toscrape.com/

Books to Scrape is a website commonly used for learning and testing web-scraping techniques.

## Current Scope

The current script processes pages 1 through 4 of the catalog:

```python
for i in range(1, 5):
```

This can be modified to scrape more pages.

For example:

```python
for i in range(1, 11):
```

would attempt to process pages 1 through 10.

## Error Handling

The script checks the HTTP response status:

```python
if response.status_code != 200:
    print("Page not found")
    continue
```

If a page cannot be retrieved successfully, the script skips that page and continues processing.

## Future Improvements

Possible improvements include:

* Scrape all available pages automatically
* Extract book availability
* Extract product URLs
* Extract book categories
* Extract UPC/product identifiers
* Extract descriptions
* Extract image URLs
* Add request timeouts
* Add exception handling
* Add logging
* Avoid duplicate records
* Save results as Excel and JSON
* Add command-line arguments
* Add configurable page ranges
* Add scraping delays and rate limiting
* Improve retry handling

## Responsible Scraping

When scraping websites, respect the website's terms, robots.txt guidance, server capacity, and applicable laws.

Avoid sending excessive requests and use reasonable delays for larger scraping jobs.

## Author

**Naeer Yasar**

GitHub: https://github.com/Naeeryasar

## Repository

https://github.com/Naeeryasar/Book-Scraping-Project
