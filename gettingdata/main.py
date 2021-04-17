import os
from time import sleep 

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from loading_season import load_all_games 
from loading_match import opening_match


games_ids = load_all_games()

# Check that 380 games where loaded
print(len(games_ids))

# Opening each game and storing stats in a dataframe
season = [opening_match(game) for game in games_ids]

# Combining all the season's results
season = pd.concat(season, ignore_index=True)

season.to_csv("2013.csv")

sleep(2)

os.system("shutdown /s /t 1")