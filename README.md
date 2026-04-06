# Cruise Price Monitor

A Python-based crawler using Playwright to monitor room prices for specific Princess Cruises voyages.

## Features
- Crawls dynamic pricing for specific state room types.
- Supports filtering for:
  - Balcony
  - Deluxe Balcony
  - Premium Deluxe Balcony
  - Mini-Suite
- Extracts the most frequent/starting price for each category.
- Composes a `mailto:` link to easily send results via email.

## Requirements
- Python 3.7+
- Playwright

## Setup
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install playwright
   playwright install chromium
   ```

## Usage
Run the crawler:
```bash
python3 crawl_prices.py
```

The script will navigate to the configured URLs, wait for the dynamic content to load, and print the identified prices for the requested room categories.
