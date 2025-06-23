import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
# import re #for advanced searching


os.makedirs("../raw/Incidence_and_Rate_of_Suicides_yearly", exist_ok=True)

for year in range(2010,2024):
    url=f"https://www.ncrb.gov.in/accidental-deaths-suicides-in-india-table-content.html?year={year}&category="
    print(url)
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')

    for link in soup.find_all('a',href=True):
        href=link['href']
        text=link.text

        # if fr"Incidence and Rate of Suicides\s*[–-]\s*{year}\s*\(State/UT\s*&\s*City-wise\)" in link.text:
        if 'Incidence and Rate of Suicides' in link.text:
            if '(State/UT & City-wise)' in link.text:
                # print("found")
                if href.endswith('.pdf'):
                    full_url = urljoin(url, href)
                    # pdf_name = full_url.split('/')[-1]
                    pdf_name=f"{year}_Incidence & Rate of Suicides.pdf"

                    print(f"Downloading: {pdf_name} ...")
                    pdf_response = requests.get(full_url)
                    with open(f"Incidence_and_Rate_of_Suicides_yearly/{pdf_name}", 'wb') as f:
                        f.write(pdf_response.content)



