import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs to scrape
urls = [
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/7755KERn.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/qckaOiWQ.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/8y5Cvg2X.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/uCubcwmG.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/lmPTt1pv.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/Sc5eCScY.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/8ChfgVz4.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/BeAUZclE.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/h25tAIrH.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/msBLHqoh.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/WgTprTOT.html",
    "https://jivraj-18.github.io/tds-jan-2025-mock-roe-1/F1hOhTwP.html"
    # Add more URLs here
]

# Function to scrape a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('div', class_='r')
    data = []
    for row in rows:
        cells = row.find_all('div', class_='c')
        for cell in cells:
            if "ROHTAK" in cell.text:
                data.append([c.text for c in cells])
                break
    return data

# Scrape all pages and combine data
combined_data = []
for url in urls:
    page_data = scrape_page(url)
    combined_data.extend(page_data)

# Save data to Excel
df = pd.DataFrame(combined_data)
df.to_excel('combined_data.xlsx', index=False)
