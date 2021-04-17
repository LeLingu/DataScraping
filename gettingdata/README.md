# Getting Data using python

The website uses HTML and CSS so time delays had to be put in to allow the page to load before scraping

.main combines the two loadings and generates a csv of the season's matches
.loading_season returns a list of all the unique ids from the season 
.loading_match returns a dataframe of the match statistics; page is loaded using its unique id
