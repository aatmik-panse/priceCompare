import requests
from bs4 import BeautifulSoup

# Set headers outside the loop
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;0.5'
}

u = input()
# Define the Amazon product URL
url = u

# Flag to indicate if scraping was successful
scraping_successful = False

# Number of times to run the code
for _ in range(100):
    # Check if scraping was already successful
    if scraping_successful:
        break

    # Make the request
    webpage = requests.get(url, headers=HEADERS)

    # Check if the request was successful (status code 200)
    if webpage.status_code == 200:
        soup = BeautifulSoup(webpage.content, 'html.parser')

        try:
            # Extract product name and price
            nam = soup.find('span', class_='a-size-large').text.strip()
            price_parent = soup.find('span', class_='a-price')
            price = price_parent.find('span', class_='a-offscreen').text

            print('From Amazon')
            print("Product Name:", nam)
            print("Price:", price)

            # Set the flag to indicate successful scraping
            scraping_successful = True
        except Exception as e:
            pass
    else:
        print(f"Failed to retrieve the Amazon webpage. Status code: {webpage.status_code}")
