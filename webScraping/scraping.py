import requests
from bs4 import BeautifulSoup
import re

url = 'http://localhost:8000/'
response = requests.get(url)
bytes_html = response.content

parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
if parsed_html.title is not None:
    print(parsed_html.title.text)

grid_heading = parsed_html.select_one('#grid-one > div > h2')
if grid_heading is not None:
    article = grid_heading.parent
    print(grid_heading.text)
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}',' ', p.text))