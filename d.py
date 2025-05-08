# python -m pip install requests
# => get data from web(html,json,xml)
#python -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import sqlite3
URL = "http://books.toscrape.com/"

def create_table():
    conn= sqlite3.connect("book.sqlite3")
    cur = con.cursor()
    cur.execute(
        """
            CREATE TABLE if not exist books(
                id integer primary key autoincrement,
                title text,
                currency text,
                price real

            );
        """
    )
    conn.commit()
    conn.close()

def insert_book(title,currency,price):
    conn = sqlite3.connect("books.sqlite3")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO book (title. currencr, price) VALUES (?,?,?)",
        (title, currency, price),
     
    )
    conn.commit()
    conn.close()


def scrape_book(url):
    response = requests.get(url)
    if response.status_code != 200:
        return

    response.encoding = response.apparent_encoding
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    book_elements = soup.find_all("article", class_="product_pod")
    for book in book_elements:
        title = book.h3.a['title']
        price_text = book.find("p", class_='price_color').text
       
        currency = price_text[0]
        price = float(price_text[1:])
        insert_book(title, currency,price)

    print("All books have been scrapped and saved to ")

scrape_book(URL)
create_table()