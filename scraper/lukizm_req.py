import requests

url = "https://cover.imglib.info/uploads/cover/oemojisangjuui/cover/a73hlURM3UlH_250x350.jpg"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'image/avif,image/webp,*/*',
  'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://mangalib.me/',
  'Sec-Fetch-Dest': 'image',
  'Sec-Fetch-Mode': 'no-cors',
  'Sec-Fetch-Site': 'cross-site',
  'Connection': 'keep-alive',
  'Cookie': '__ddg1_=OpVhI2vpPNAQTb2Bckb8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
