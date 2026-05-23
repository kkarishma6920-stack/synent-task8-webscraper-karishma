import requests
from bs4 import BeautifulSoup
import pandas as pd
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "=== WEB SCRAPER ===")

# Website URL
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("span", class_="text")

# Store data
data = []

for quote in quotes:

    text = quote.text

    print(Fore.GREEN + text)

    data.append({"Quote": text})

# Save to CSV
df = pd.DataFrame(data)

df.to_csv("quotes.csv", index=False)

print(Fore.CYAN + "\nData saved to quotes.csv")