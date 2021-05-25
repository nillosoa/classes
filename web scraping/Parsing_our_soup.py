from bs4 import BeautifulSoup
import requests


search = input("Enter search term: ")
params = {"q": search, "first": "13"}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_hf = item.find("a").attrs["href"]

    if item_text and item_hf:
        print(item_text)
        print(item_hf)
