# This was adapted from a lecture in ATBSWP Udemy's course.
# The original project doesn't work anymore. So, I decided to make
# this alternative as project since Selenium and bs4 were in the same
# chapter.


from selenium import webdriver
import pyperclip

priceSelector = 'span.a-size-medium.a-color-price.offer-price.a-text-normal'
nameSelector  = '#productTitle'

def getAmazonPrice(url):
    # Start's a selenium's chrome driver instance and goes to given url
    browser = webdriver.Chrome()
    browser.get(url)
    # Looks for the css selectors(priceSelector and nameSelector)
    priceElem = browser.find_element_by_css_selector(priceSelector)
    titleElem = browser.find_element_by_css_selector(nameSelector)
    # Saves them before quiting the browser
    price = priceElem.text
    title = titleElem.text
    browser.quit()
    # Then returns them as a tuple
    return (title, price)

url = pyperclip.paste()
try:
    title, price = getAmazonPrice(url)
    amazonUrl = url[:url.index('/', 9)]
    print('Price for {} at {} is {}.'.format(title, amazonUrl, price))
except Exception as e:
    print('Could not find price for given url.')
    print(url)
    print('Error message:')
    print(e)