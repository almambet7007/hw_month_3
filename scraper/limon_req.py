import requests

url = "https://fonts.gstatic.com/s/lora/v32/0QIvMX1D_JOuMwr7Iw.woff2"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8',
  'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'identity',
  'Origin': 'https://limon.kg',
  'Connection': 'keep-alive',
  'Referer': 'https://fonts.googleapis.com/',
  'Sec-Fetch-Dest': 'font',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
