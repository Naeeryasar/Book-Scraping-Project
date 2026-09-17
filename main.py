import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

header = {"User-Agent": "Mozilla/5.0"}
all_book = []