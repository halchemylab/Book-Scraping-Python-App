import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# Function to scrape a single page
def scrape_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_number}: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]  # Get the second class for the rating (e.g., "Three")
        books.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating
        })
    
    return books

# Function to scrape multiple pages
def scrape_books(pages_to_scrape):
    all_books = []
    for page_number in range(1, pages_to_scrape + 1):
        print(f"Scraping page {page_number}...")
        books = scrape_page(page_number)
        if not books:  # Stop if the page is invalid or scraping fails
            break
        all_books.extend(books)
    return all_books

# Save data to a CSV file
def save_to_csv(data, filename):
    keys = data[0].keys() if data else []
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    pages_to_scrape = 3  # Adjust the number of pages to scrape
    scraped_books = scrape_books(pages_to_scrape)

    if scraped_books:
        save_to_csv(scraped_books, 'books.csv')
        print(f"Scraped data saved to 'books.csv'!")
    else:
        print("No data scraped.")
