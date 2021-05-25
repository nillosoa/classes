from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests


search = input("Search for: ")
params = {"q": search}
r = requests.get("https://wwww.bing.com/images/search", params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for item in links:
    img_obj = requests.get(item.attrs["href"])
    print("Getting", item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]

    img = Image.open(BytesIO(img_obj.content))
    img.save("scraped_images/" + title, img.format)