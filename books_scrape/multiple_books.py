import requests
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

items = soup.find_all('article', class_='product_pod')

csv_file = open('books.csv', 'w')
book_headers = ['BookName', 'BookPrice', 'Availability']
csv_writer = csv.writer(csv_file)
csv_writer.writerow(book_headers)

for item in items:
    book_items = []
    book_name = item.find('h3').a['title']
    book_items.append(book_name)
    other_features = item.find('div', class_='product_price')
    book_price = other_features.find('p', class_='price_color').text
    book_items.append(book_price)
    book_availability = other_features.find('p', class_='instock availability').text
    book_items.append(book_availability)
    csv_writer.writerow(book_items)
csv_file.close()
    
    


# print(books)
# print()
# print(prices)
# print()
# print(availability)