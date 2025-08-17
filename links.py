import requests

url = "https://web.archive.org/web/timemap/json?url=twitter.com%2FNekroVevo&matchType=prefix&collapse=urlkey&output=json&fl=original%2Cmimetype%2Ctimestamp%2Cendtimestamp%2Cgroupcount%2Cuniqcount&filter=!statuscode%3A%5B45%5D..&limit=10000000&from=201902&to=202011&_=1755293069136"

payload = {}
headers = {
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'no-cache',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://web.archive.org/web/202009*/twitter.com/NekroVevo*',
  'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest',
  'Cookie': 'wb-p-SERVER=wwwb-app224; wb-cdx-SERVER=wwwb-app208; donation-identifier=bea4320a4776fb2c84a3999cc69ec714; wb-cdx-ui-SERVER=wwwb-app205; view-search=tiles; showdetails-search=; abtest-identifier=aa344537511d7d4184bf39f0bc72bb24'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import json

rows = json.loads(response.text)
# Optionally save to a JSON file
with open("nekrovevo_captures.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)
