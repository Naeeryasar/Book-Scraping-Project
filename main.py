import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

header = {"User-Agent": "Mozilla/5.0"}
all_book = []

for i in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    print(f"Scrapping Page {i}")

    response = requests.get(url, headers=header)

    if response.status_code != 200:
        print("Page not found")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")