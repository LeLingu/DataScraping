from time import sleep 
import re

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup

# Given the season's page on flashscore each game's unique id is scraped and stored in a returned list

def load_all_games():

    url = 'https://www.flashscore.com/football/england/premier-league-2013-2014/results/'
    browser = webdriver.Edge(executable_path= "msedgedriver.exe")
    browser.get(url)

    button = browser.find_element_by_link_text('Show more matches')

    while 2>1:
        try:
            browser.execute_script("arguments[0].click();", button)
            sleep(1)
        except StaleElementReferenceException:
            sleep(8) 
            break       

    html = browser.page_source
    Soup = BeautifulSoup(html, 'html.parser')

    browser.close()

    pattern = re.compile('^g_1_')

    games = Soup.find_all(id= pattern)

    games_id = [game.get('id')[4:] for game in games]

    return(games_id)
