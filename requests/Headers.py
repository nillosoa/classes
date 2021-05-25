#https://developers.google.com/url-shortener/v1/getting_started
import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
params = {"key": "AIzaSyBJVsfHnLMcq_qp2iQTKZCf1vlBOTwKFVc"}
payload = {"longUrl": "http://example.com/"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, params=params, json=payload, headers=headers)

print(r.headers)