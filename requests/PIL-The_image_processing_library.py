import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://cdn.dribbble.com/users/5031/screenshots/3713646/attachments/832536/wallpaper_mikael_gustafsson.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

path = "image1." + image.format

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")
