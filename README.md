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
```
## 📁 Project Structure
```sh
ncbr_report/
│
├── raw/                       # For storing downloaded PDFs
|   |---2021/
|   |---2022/
|   |---Incidence_and_Rate_of_Suicides_yearly/
├── processed/                 # For cleaned CSVs
|   |---processed_Incidence_and_Rate_of_Suicides_yearly
|   |---camelot(extract tabels from pdfs).py
|   |---Separate(state and UT).py
├── scraper/                   # Your Scrapy or BS4 spider code
│   ├── __init__.py
│   ├── BS4(2021&2022).py         # Main script for scraping PDFs
│   |---BS4(Incidence&rate_of_sucides).py
|
├── cleaner/                   # Data extraction and cleaning scripts
│   ├---cleaned_data/
│   ├── DataCleaning(Combined_clean).py    
│   ├── DataCleaning(Tidy_Combined).py          
│   |---DataCleaning(As_Per_Format_of_Final_Data).py
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

