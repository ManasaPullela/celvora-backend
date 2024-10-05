import requests
from bs4 import BeautifulSoup

# Step 1: Make a Request to the Website
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML Content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find All Book Containers
    books = soup.find_all('article', class_='product_pod')

    # Step 4: Extract and Display Book Details
    for book in books:
        # Get the title
        title = book.h3.a['title']
        
        # Get the price
        price = book.find('p', class_='price_color').text
        
        # Print out the book title and price
        print(f"Book Title: {title}, Price: {price}")
else:
    print("Failed to retrieve the website")

