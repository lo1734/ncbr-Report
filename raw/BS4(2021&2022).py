import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re #for advanced searching (only specific files)

# url='https://www.ncrb.gov.in/accidental-deaths-suicides-in-india-table-content.html?year=2022&category=Accidents+in+India'
url="https://www.ncrb.gov.in/accidental-deaths-suicides-in-india-table-content.html?year=2022&category=Suicides+in+India"

#sending GET request to that target page
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

#create folder to save a raw PDFs
# os.makedirs("/Users/lohith/Desktop/ncbr-Report/raw/2022",exist_ok=True)
# os.makedirs("2021",exist_ok=True)
os.makedirs("2022",exist_ok=True)

#find links that end with .pdf
for link in soup.find_all('a',href=True):
    href = link['href']
    text = link.text
    if re.search(r'Table.*\.pdf$',href):
        if href.endswith('.pdf'):
            full_url = urljoin(url, href)  # make the url full, if href is relative
            pdf_name = full_url.split('/')[-1]

            print(f"Downloading {pdf_name}...")
            pdf_response = requests.get(full_url)
            # with open(f"2021/{pdf_name}", 'wb') as f:
            #     f.write(pdf_response.content)
            with open(f"2022/{pdf_name}",'wb') as f:
                f.write(pdf_response.content)


