from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get('https://toxicwap.com')

movies = driver.find_element(By.LINK_TEXT, 'Movies')
movies.click()

movies = driver.find_elements(By.TAG_NAME, 'li')

movie_file = open('all_series.txt', 'a')
for movie in movies:
    movie_file.write(movie.find_element(By.TAG_NAME, 'a').text)
    movie_file.write('\n')

while True:
    next_page = driver.find_element(By.LINK_TEXT, 'Next Page')
    if next_page:
        next_page.click()
        movies = driver.find_elements(By.TAG_NAME, 'li')
        movie_file = open('all_series.txt', 'a')
        for movie in movies:
            movie_file.write(movie.find_element(By.TAG_NAME, 'a').text)
            movie_file.write('\n')
    else:
        movie_file.write('THE END')
time.sleep(12) 