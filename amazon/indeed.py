from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://indeed.com')
signin_link = driver.find_element(By.LINK_TEXT, 'Sign in')
signin_link.click()
current_url = driver.current_url
driver.get(current_url)

google_signin_link = driver.find_element(By.LINK_TEXT, 'Continue with Google')
google_signin_link.click()
# signin_link = driver.find_element(By.LINK_TEXT, 'Sign In')
# signin_link.click()
# current_url = driver.current_url
# driver.get(current_url)


time.sleep(2000)