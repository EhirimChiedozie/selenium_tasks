from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()

driver.get('https://newtoxic.com/New_Movies/')

ul = driver.find_element(By.CLASS_NAME, 'ui-listview')
list_tags = ul.find_elements(By.TAG_NAME, 'li')
action_movies = []
for i in list_tags:
    i.click()
    movie_description = requests.get(driver.current_url).text
    if "Action" in movie_description:
        action_movies.append(i)

print(action_movies)