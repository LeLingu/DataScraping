from time import sleep 

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from urllib.parse import urljoin



url = 'https://www.flashscore.com/match/zDR1CCoh/#match-summary'

browser = webdriver.Edge("msedgedriver.exe")
browser.get(url)

# clicking stats on the page
button1 = browser.find_element_by_link_text('Statistics')
sleep(1)
browser.execute_script("arguments[0].click();", button1)
button2 = browser.find_element_by_link_text('Match')
browser.execute_script("arguments[0].click();", button2)

sleep(2)
browser.close()


# button2 = browser.find_element_by_link_text('Match')
# try:
#     sleep(2)
#     browser.execute_script("arguments[0].click();", button2)
# except:
#     print("NA")

# sleep(1)

# html = browser.page_source
# Soup = BeautifulSoup(html, 'html.parser')
# browser.close()