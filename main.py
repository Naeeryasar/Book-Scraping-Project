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

for j in books:
        title_tag = j.find("h3").find("a")

        if title_tag:
            title = title_tag["title"]
        else:
            title = "N/A"

        price_tag = j.find("p", class_="price_color")

        if price_tag:
            price = price_tag.get_text(strip=True)
        else:
            price = "N/A"

        rating_tag = j.find("p", class_="star-rating")

        if rating_tag:
            rating = rating_tag["class"][1]
        else:
            rating = "N/A"

        product_link = j.find("h3").find("a")["href"]

        if product_link:
            product_url = urljoin(url, product_link)
            product_page = requests.get(product_url, headers=header)
            product_soup = BeautifulSoup(product_page.text, "html.parser")

            available = product_soup.find(
                "p", class_="instock availability"
            ).get_text(strip=True)
        else:
            available = "N/A"

        all_book.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
        })

df = pd.DataFrame(all_book, columns=["Title", "Price", "Rating"])