import requests

url = "https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
