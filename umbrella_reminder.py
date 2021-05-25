#! python3
# umbrella_reminder.py - scrapes yahoo given weather location in search of a rain
# and sends a sms to the given number in case true.
# Use: umbrella_reminder.py number [location...]

from twilio.rest import Client
import requests, bs4, sys

if len(sys.argv) < 3:
    print('Please specify a cell number and location to beggin with.')
    sys.exit()

if not sys.argv[1].isnumeric():
    print('Please specify a phone number(or at lest a integer, the code won\'t verify this).')
    sys.exit()

if not ''.join(sys.argv[2:]).isalpha():
    print('I don\'t believe any city, state, or country has an integer in it\'s name...')
    sys.exit()

cell  = '+' + sys.argv[1]
local = sys.argv[2:]
twilio_account_sid = ''
twilio_auth_token  = ''
twilio_from_ = ''

# First, I'll be googling the location to find it's yahoo weather url.
search_params = {'q': ' '.join(local + ['forecast', 'site:yahoo.com'])}
search_req = requests.get('https://www.google.com/search', params=search_params)

search_soup = bs4.BeautifulSoup(search_req.text, 'html.parser')
urls = search_soup.select('#search a')
weather_url  = None 
for url in urls:
    url = url.get('href')
    if '/url?q=' in url: # Google's no JS:(
        url = url.replace('/url?q=', '')
    if '&' in url:
        url = url[0:url.find('&')]
    if url.startswith('https://www.yahoo.com/news/weather/'):
        weather_url = url
        break

if not weather_url:
    print('Could not find given location. Try another term.')
    sys.exit()

print('I have found the following url while googling for %s:\n%s' %(' '.join(local), weather_url))
# Now, I'll be scrapping the page to get info about the weather
weather_session = requests.session() # First I tried with accuweather, that needed a 'browser' with cookies support. Keeping for posteriority
weather_session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Accept-Language': 'en-US;en;q=0.9',
    'Accept-Encoding': 'gzip, deflate'
})
weather_req = weather_session.get(weather_url)
weather_soup = bs4.BeautifulSoup(weather_req.text, 'html.parser')

# This is not great, I may look for another way of storying this 'weather' kind of data
weather_city    = weather_soup.select_one('.location .city').text
weather_country = weather_soup.select_one('.location .country').text
weather_description = weather_soup.select_one('span.description').text
weather_temperature = weather_soup.select_one('div.now').text
weather_detail  = weather_soup.select_one('#weather-detail > div > div.description').find_all('p')
weather_today   = weather_detail[1].text
weather_tonight = weather_detail[0].text

print('Great! The forecast for %s, %s is %s and the temperature is %s.' %(weather_city, weather_country, weather_description, weather_temperature))
# Let's chat
if any(n in weather_today for n in ['Rain', 'Thunderstorms']): #Generators hell ya
    print('Possible thunderstorm.\nSending SMS...')
    client = Client(twilio_account_sid, twilio_auth_token)
    message_body = """Hi!, It seens that is going to have a %s in %s today.
This is just a reminder for you to carry an umbrella.""" %(weather_description, weather_city)
    message = client.messages.create(
        to=cell,
        from_=twilio_from_,
        body=message_body
    )
    print('Twilio\'s status:', message.status)


