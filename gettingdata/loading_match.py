from time import sleep 
import re

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Opening each game's page from the unique id list from loading_season and returning the stats as a dataframe

def opening_match(unique_id):

    url = 'https://www.flashscore.com/match/' + unique_id + '/#match-summary/match-statistics/0'

    browser = webdriver.Edge("msedgedriver.exe")
    browser.get(url)

    # clicking stats on the page
    # try:
    #     button1 = browser.find_element_by_link_text('Statistics')
    #     browser.execute_script("arguments[0].click();", button1)
    #     sleep(1)
    #     button2 = browser.find_element_by_link_text('Match')
    #     browser.execute_script("arguments[0].click();", button2)
    # except:
    #     print("NA")

    sleep(1)

    html = browser.page_source
    Soup = BeautifulSoup(html, 'html.parser')
    browser.close()

    # The two game stats that aren't standardised
    teams = Soup.findAll("div", {"class": "participantName___3lRDM1i"})
    home_team = teams[0].a.text
    away_team = teams[1].a.text

    goals = Soup.findAll("div", {"class": "wrapper___3rU3Jah"})
    home_goals = goals[0].text[0]
    away_goals = goals[0].text[2]

    # Setting up the dataframe
    stats = { "Home_team": [home_team],

            "Away_team": [away_team],

            "Goals_Home_team": [home_goals],

            "Goals_Away_team": [away_goals]

    }
    match = pd.DataFrame(stats, columns= ['Home_team', 'Away_team', 'Goals_Home_team', 'Goals_Away_team'])

    pattern1 = re.compile('^homeValue')
    pattern2 = re.compile('^categoryName')
    pattern3 = re.compile('^awayValue')

    
    # Getting at the stats on the page
    containers = Soup.findAll("div", {"class":"statCategory___33LOZ_7"})

    for i in containers:

        stat = i.find("div", {"class": pattern2}).text

        home_value = i.find("div", {"class": pattern1}).text

        away_value = i.find("div", {"class": pattern3}).text

        match[stat+"_Home_team"] = home_value

        match[stat+"_Away_team"] = away_value


    return(match)

