import requests
from bs4 import BeautifulSoup

url = input('Enter the url')

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h3')

for index, headline in enumerate(headlines):
    print(f"{index + 1}. {headline.get_text(strip=True)}")
