# NCRB-Report

# 📊 NCRB Suicides Data Scraper & Cleaner

This project scrapes suicide statistics PDFs from the [NCRB (National Crime Records Bureau)](https://ncrb.gov.in) website, extracts tabular data, and transforms it into a clean, analysis-ready CSV format.

---

## 📁 Project Structure
```sh
ncrb_suicides_scraper/
│
├── raw/                       # For storing downloaded PDFs
├── processed/                 # For cleaned CSVs
├── scraper/                   # Your Scrapy or BS4 spider code
│   ├── __init__.py
│   ├── pdf_scraper.py         # Main script for scraping PDFs
│
├── cleaner/                   # Data extraction and cleaning scripts
│   ├── __init__.py
│   ├── extract_tables.py      # Camelot logic to extract data
│   ├── clean_data.py          # Logic to clean and standardize the tables
│
├── utils/                     # Helper functions (optional)
│   └── download_helpers.py
│
├── main.py                    # Entry-point script
├── requirements.txt           # Dependencies
└── README.md                  # Instructions to run the project
```
