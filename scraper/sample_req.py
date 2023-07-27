import requests

url = "https://www.mozilla.org/media/protocol/img/logos/mozilla/vpn/logo-flat-white.7310b86a6954.svg"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'image/avif,image/webp,*/*',

}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
