from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from perm import rightPass


driver = webdriver.Chrome()

driver.get('http://localhost:5000/login')

# with open('password.txt', 'r') as password_file:
#     content = password_file.readlines()
# password_list = []
# for i in content:
#     i = i.replace('\n', '')
#     password_list.append(i)



email_field = driver.find_element(By.ID, 'email')
email_field.clear()
email_field.send_keys('dera@gmail.com')

correct_password = open('rightbcot_password.txt', 'w')

for password in rightPass:
    password_field = driver.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(password)
    correct_password.write(password+'\n')
    submit_field = driver.find_element(By.ID, 'submit')
    submit_field.click()

correct_password.close()

time.sleep(1200)