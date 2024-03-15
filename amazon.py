import csv
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;0.5'})


url = 'https://www.amazon.in'
driver.get(url)

def get_url(search_term):
    """Generate a url for search"""
    template = 'https://www.amazon.in/s?k={}'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)
print("Enter the Product Name to be searched : ")
n=input()
url = get_url(n)
print(url)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all('div', {'data-component-type': 's-search-result'})
print(len(results))

item = results[0]
atag = item.h2.a
description = atag.text.strip()
url = 'https://www.amazon.com' + atag.get('href')
price_parent = item.find('span', 'a-price')
price = price_parent.find('span', 'a-offscreen').text
rating = item.i.text


def extract_record(item):
    try:
        atag = item.h2.a
        description = atag.text.strip()
        url = 'https://www.amazon.com' + atag.get('href')
    except AttributeError:
        pass
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return
    try:
        rating = item.i.text
    except AttributeError:
        rating=''

    result = (description,price,rating,url)
    return result

records = []
results = soup.find_all('div', {'data-component-type': 's-search-result'})

for item in results:
    record = extract_record(item)
    if record:
        records.append(record)

records[0]
# for row in records:
#     print(row[1])
print("Enter the filename: ")
x = input()

with open(x+'.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Description', 'Price', 'Rating', 'Url'])
    writer.writerows(records)