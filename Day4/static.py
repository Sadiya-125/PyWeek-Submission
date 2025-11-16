import requests
from bs4 import BeautifulSoup

url = "https://tsigmjcet.in/"
page = requests.get(url)
soup=BeautifulSoup(page.text, "html.parser")

print("first heading")
print(soup.find("h2").text)

print("all heading on the page")
for h in soup.find_all("h2"):
    print("-",h.text)

for a in soup.find_all("a"):
    print("-",a.get_text(strip=True),":",a.get("href"))

