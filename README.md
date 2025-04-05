# Booking.com Hotel Data Scraper 🏨

This Python script scrapes hotel data from Booking.com for a specified location and saves it into a CSV file. The data includes:

- Hotel Name
- Location
- Price
- Rating
- Reviews
- Link to the Hotel Page

## ✨ Features

- Scrapes hotel listings based on the provided Booking.com URL.
- Extracts and stores hotel name, location, price, rating, reviews, and direct link.
- Saves data in a CSV file named `hotels.csv`.
- Displays hotel data in the console as well.

## 📦 Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `csv` (built-in)

Install dependencies using pip:

```bash
pip install requests beautifulsoup4 lxml
