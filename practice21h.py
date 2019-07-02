import requests

from bs4 import BeautifulSoup # External library for Parsing HTML Data.

url = "https://twitter.com/dna"

response = requests.get(url)
#print(response.text)

# HTML Parsing : From HTML code extracts the desired / meaningful information .

soup = BeautifulSoup(response.text, "html.parser")
print("Type of Soup is:", type(soup) )
print("================================")

print("Title is:", soup.title.text)
print("=================================")

divTags = soup.find_all("div", class="js-tweet-text-container")
for tag in pTags:
    print(tag)
    print("------------------------------")