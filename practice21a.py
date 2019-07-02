import requests

url = "https://twitter.com/dna"

response = requests.get(url)
print(response.text)

# HTML Parsing : From HTML code extracts the desired / meaningful information .