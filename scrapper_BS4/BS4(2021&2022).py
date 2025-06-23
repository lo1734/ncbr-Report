import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re #for advanced searching


for year in ["2021","2022"]:
    url = f"https://www.ncrb.gov.in/accidental-deaths-suicides-in-india-table-content.html?year={year}&category="
    # sending GET request to that target page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # create folder to save a raw PDFs
    os.makedirs(f"../raw/{year}", exist_ok=True)

    # find links that end with .pdf
    for link in soup.find_all('a', href=True):
        href = link['href']
        text = link.text

        #filtering on pdf's which are containg Table in the file_name
        if re.search(r'Table.*\.pdf$', href):
            if href.endswith('.pdf'):
                full_url = urljoin(url, href)  # make the url full, if href is relative
                pdf_name = full_url.split('/')[-1]

                print(f"Downloading {pdf_name}...")
                pdf_response = requests.get(full_url)
                with open(f"../raw/{year}/{pdf_name}", 'wb') as f:
                    f.write(pdf_response.content)





