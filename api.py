import requests

headers = {
    "User-Agent": "NotionCS2Tracker/1.0 (ganbaatarpurevochir1@gmail.com)",
    "Accept-Encoding": "gzip"  # ✅ This tells the server you accept compressed responses
}

url = "https://liquipedia.net/counterstrike/api.php?action=cargoquery&tables=Tournaments&fields=name,startdate,enddate&format=json"

response = requests.get(url, headers=headers)

print(response.json())  # Prints tournament data

