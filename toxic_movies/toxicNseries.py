from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://toxicwap.com')
tv_series = driver.find_element(By.LINK_TEXT, 'TV Series')
tv_series.click()

letter_n = driver.find_element(By.LINK_TEXT, 'N')
letter_n.click()

movies = driver.find_elements(By.TAG_NAME, 'li')

movie_file = open('toxic_movies.txt', 'a')
for movie in movies:
    movie_file.write(movie.find_element(By.TAG_NAME, 'a').text)
    movie_file.write('\n')

while True:
    next_page = driver.find_element(By.LINK_TEXT, 'Next')
    if next_page:
        next_page.click()
        movies = driver.find_elements(By.TAG_NAME, 'li')
        movie_file = open('toxic_movies.txt', 'a')
        for movie in movies:
            movie_file.write(movie.find_element(By.TAG_NAME, 'a').text)
            movie_file.write('\n')
    else:
        movie_file.write('THE END')
time.sleep(12)