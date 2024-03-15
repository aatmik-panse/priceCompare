import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_website(url, website_name):
    try:
        HEADERS = ({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;0.5'
        })

        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        # Extract product name and price
        nam = soup.find('span', 'a-size-large product-title-word-break')
        price_parent = soup.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text

        return website_name, nam, price
    except Exception as e:
        print(f"Error while scraping {website_name}: {str(e)}")
        return website_name, '', ''


def flipkart_scrape_website(url, website_name):
    try:
        HEADERS = ({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;0.5'
        })

        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        # Extract product name and price
        nam = soup.find('span', 'B_NuCI').text
        price = soup.find('div', '_30jeq3 _16Jk6d').text

        return website_name, nam, price

    except Exception as e:
        print(f"Error while scraping {website_name}: {str(e)}")
        return website_name, '', ''


def convert_to_numeric(price_string):
    try:
        price_numeric = float(price_string.replace('₹', '').replace(',', ''))
        return price_numeric
    except ValueError:
        return 0.0  # Return 0.0 if the conversion fails


print("Please enter the link from Amazon")
url = input()
print("Please enter the link from Flipkart")
Flipkarturl = input()

# Scrape data from Amazon and Flipkart
amazon_data = scrape_website(url, 'Amazon')
flipkart_data = flipkart_scrape_website(Flipkarturl, 'Flipkart')

# Convert prices to numeric (or 0.0 if conversion fails)
price_amazon_numeric = convert_to_numeric(amazon_data[2])
price_flipkart_numeric = convert_to_numeric(flipkart_data[2])

# Calculate the price difference
price_difference = abs(price_amazon_numeric - price_flipkart_numeric)

# Create a DataFrame
data = {
    'Website': [amazon_data[0], flipkart_data[0], 'Price Difference'],
    'Product Name': [amazon_data[1], flipkart_data[1], ''],
    'Price': [amazon_data[2], flipkart_data[2], price_difference]
}

# Compare prices and update the "Product Name" column
if price_amazon_numeric < price_flipkart_numeric:
    data['Product Name'][2] = 'Price in Amazon is Cheaper by'
elif price_amazon_numeric > price_flipkart_numeric:
    data['Product Name'][2] = 'Price in Flipkart is Cheaper by'
else:
    data['Product Name'][2] = 'Prices are the Same'

df = pd.DataFrame(data)
x = input()
# Save the DataFrame to a CSV file
df.to_csv(x+'.csv', index=False)
