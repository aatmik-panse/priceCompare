import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_website(url, website_name):
    try:
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;0.5'
        }

        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        nnn = soup.find('span', 'a-size-large product-title-word-break').text
        price_parent = soup.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text

        return website_name, nnn, price
    except Exception as e:
        pass
        return website_name, '', ''

def flipkart_scrape_website(url, website_name):
    try:
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;0.5'
        }

        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        nnn = soup.find('span', 'B_NuCI').text
        price = soup.find('div', '_30jeq3 _16Jk6d').text

        return website_name, nnn, price
    except Exception as e:
        pass
        return website_name, '', ''

def convert_to_numeric(price_string):
    try:
        price_numeric = float(price_string.replace('₹', '').replace(',', ''))
        return price_numeric
    except ValueError:
        return 0.0

amazon_scraping_successful = False
flipkart_scraping_successful = False

print("Please enter the link from Amazon")
url = input()
for _ in range(50):
    amazon_data = scrape_website(url, 'Amazon')

    if amazon_data[1]:
        amazon_scraping_successful = True
        break

print("Please enter the link from Flipkart")
Flipkarturl = input()
for _ in range(5):
    flipkart_data = flipkart_scrape_website(Flipkarturl, 'Flipkart')

    if flipkart_data[1]:
        flipkart_scraping_successful = True
        break

if amazon_scraping_successful and flipkart_scraping_successful:
    price_amazon_numeric = convert_to_numeric(amazon_data[2])
    price_flipkart_numeric = convert_to_numeric(flipkart_data[2])

    price_difference = abs(price_amazon_numeric - price_flipkart_numeric)

    data = {
        'Website': [amazon_data[0], flipkart_data[0], 'Price Difference'],
        'Product Name': [amazon_data[1], flipkart_data[1], ''],
        'Price': [amazon_data[2], flipkart_data[2], price_difference]
    }

    if price_amazon_numeric < price_flipkart_numeric:
        data['Product Name'][2] = 'Price in Amazon is Cheaper by'
    elif price_amazon_numeric > price_flipkart_numeric:
        data['Product Name'][2] = 'Price in Flipkart is Cheaper by'
    else:
        data['Product Name'][2] = 'Prices are the Same'

    df = pd.DataFrame(data)

    x = input("Enter the filename: ")
    df.to_csv(x + '.csv', index=False)
else:
    print("Scraping was unsuccessful for one or both websites.")