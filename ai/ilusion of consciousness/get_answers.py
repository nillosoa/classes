
import sys
import time

from shutil import which
from pathlib import Path

from bs4 import BeautifulSoup
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Fetcher:
    def __init__(self, url, gecko_path=''):
        self.gecko_path = (
                gecko_path or (
                    str(Path.home()) + '/geckodriver'))

        self.options = Options()

        self.options.binary = which('firefox')
        self.options.profile = None
        self.options.add_argument('--headless')

        self.driver = webdriver.Firefox(
            options=self.options,
            executable_path=self.gecko_path)
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            self.driver.wait.until(
                EC.presence_of_element_located(
                        (By.CLASS_NAME, 'gsfi')))
        except Exception as err:
            print(err)
            return 'Something happened while looking for that.'

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        answer = soup.select('[data-tts]')

        self.driver.quit()

        if answer:
            return answer[0].get_text()

        return 'Sorry, I couldnt find that.'

