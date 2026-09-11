import requests
from bs4 import BeautifulSoup

URL = "https://allnewsinfo.co.uk/"

def fetch_headlines():
  response = requests.get(URL, timeout=10)
  response.raise_for_status()
  soup = BeautifulSoup(response.text, "html.parser")
  tags = soup.find_all(["h1", "h2", "h3"])
  return [tag.get_text(strip=True) for tag in tags if tag.get_text(strip=True)]

if __name__ == "__main__":
  for i, headline in enumerate(fetch_headlines(), start=1):
    print(f"{i}. {headline}")
