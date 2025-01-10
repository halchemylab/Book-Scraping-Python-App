# Books Scraper

This project is a web scraper built with Python that extracts book data from [Books to Scrape](http://books.toscrape.com). The data includes book titles, prices, availability, and ratings, which are saved into a CSV file for analysis.

---

## Features

- Scrapes multiple pages from the website.
- Extracts the following details for each book:
  - **Title**
  - **Price**
  - **Availability**
  - **Rating** (converted to numerical format).
- Saves the scraped data into a `books.csv` file.

---

## Requirements

The project requires the following dependencies:

- `requests`
- `beautifulsoup4`

You can install them using:

```bash
pip install -r requirements.txt
```

---

## How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/books-scraper.git
   cd books-scraper
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv books_scraper_env
   source books_scraper_env/bin/activate  # For macOS/Linux
   books_scraper_env\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**
   ```bash
   python books_scraper.py
   ```

5. **Adjust Pages to Scrape**
   - Modify the `pages_to_scrape` variable in the `if __name__ == "__main__"` block to scrape the desired number of pages.

---

## Output

- The scraped data is saved to a CSV file named `books.csv` in the project directory.
- Columns in the CSV:
  - **Title**: Name of the book.
  - **Price**: Price of the book (in EUR).
  - **Availability**: Stock status.
  - **Rating**: Numerical representation of the rating (1-5).

---

## Example CSV Output

| Title                             | Price   | Availability    | Rating |
|-----------------------------------|---------|-----------------|--------|
| A Light in the Attic             | €51.77  | In stock        | 3      |
| Tipping the Velvet               | €53.74  | In stock        | 1      |
| Soumission                       | €50.10  | In stock        | 1      |

---

## Future Improvements

- Automatically scrape all available pages without specifying `pages_to_scrape`.
- Add error handling for network issues or unexpected HTML changes.
- Extend functionality to handle dynamic websites using tools like `Selenium` or `Playwright`.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgements

- Website used for scraping: [Books to Scrape](http://books.toscrape.com)
- Python libraries: `requests`, `beautifulsoup4`