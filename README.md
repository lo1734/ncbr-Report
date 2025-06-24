# NCRB-Report

# 📊 NCRB Suicides Data Scraper & Cleaner

This project scrapes suicide statistics PDFs from the [NCRB (National Crime Records Bureau)](https://ncrb.gov.in) website, extracts tabular data, and transforms it into a clean, analysis-ready CSV format.

---


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/lo1734/ncbr-Report.git
cd ncbr_suicides_scraper

## 📁 Project Structure
```sh
ncbr_report/
│
├── raw/                       # For storing downloaded PDFs
├── processed/                 # For cleaned CSVs
├── scraper/                   # Your Scrapy or BS4 spider code
│   ├── __init__.py
│   ├── pdf_scraper.py         # Main script for scraping PDFs
│
├── cleaner/                   # Data extraction and cleaning scripts
│   ├
│   ├── extract_tables.py      # Camelot logic to extract data
│   ├── clean_data.py          # Logic to clean and standardize the tables
│   |---CleanedData(Requirements).py
│
├── requirements.txt           # Dependencies
└── README.md                  # Instructions to run the project
```

## 🧱 Tech Stack

This project is built entirely in **Python**, using the following libraries and tools:

---

### 🌐 Web Scraping

| Library          | Usage                                                 |
|------------------|--------------------------------------------------------|
| `requests`       | Sending HTTP GET requests to fetch NCRB web pages     |
| `beautifulsoup4` | Parsing HTML to locate PDF links                      |
| `re` (regex)     | Matching patterns in PDF titles and text content      |
| `urllib.parse`   | Resolving and joining relative and absolute URLs      |

---

### 📄 PDF Handling & Table Extraction

| Library             | Purpose                                                     |
|---------------------|-------------------------------------------------------------|
| `camelot-py[cv]`    | Extracting tables from PDFs using the Stream parsing method |
| `ghostscript`       | Required backend for Camelot PDF rendering and processing   |
| `pdfplumber` (optional) | Alternative library for extracting text and tables     |

---

### 🧹 Data Cleaning & Transformation

| Library     | Usage                                                              |
|-------------|---------------------------------------------------------------------|
| `pandas`    | Cleaning, merging, reshaping tabular data into analysis-ready form |
| `numpy`     | Optional: Handling missing values and numeric conversions          |
| `os`, `glob`| Navigating directories and batch-processing files                  |

---

### 📦 Environment & Package Management

| Tool              | Description                                  |
|-------------------|----------------------------------------------|
| `virtualenv` / `venv` | Creates isolated Python environments     |
| `pip`             | Installs required packages                   |
| `requirements.txt`| Lists all dependencies used in the project   |

---

> 📌 All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt

