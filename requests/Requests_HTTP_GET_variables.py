import requests

params = {"q": "pizza"}
r = requests.get("https://google.com/search", params=params)

print("Status:", r.status_code)
print("Url:", r.url)

f = open("page.html", "w+")
f.write(r.text)