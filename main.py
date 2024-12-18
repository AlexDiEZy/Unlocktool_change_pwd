import time
import seleniumbase
import selenium

from anticaptchaofficial.recaptchav2enterpriseproxyless import *

from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from const import token_api
from const import URI
from const import site_clean
from const import change_password_page
from const import account_page



driver = Driver(uc= True)

current_login = 'Razlock_phone'
current_password = 'Hrenovoo24'

source_page = driver.get(URI)
driver.type("#id_username", current_login)
driver.type("#id_password", current_password)


time.sleep(5)


solver = recaptchaV2EnterpriseProxyless()
solver.set_verbose(1)
solver.set_key(token_api)
solver.set_website_url(URI)
solver.set_website_key(site_clean)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print('g_response'+g_response)
else:
    print('Error' + solver.error_code)

recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response')
driver.execute_script(f'arguments[0].value = "{g_response}";', recaptcha_response_element)


WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/div[1]/div[1]/form/button'))
).click()

new_password = 'Hrenovoo24'

driver.get(change_password_page)
time.sleep(1)
driver.type("#id_old_password", current_password)
driver.type("#id_new_password1", new_password)
driver.type("#id_new_password2", new_password)

WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/div/form/button'))
).click()


driver.get(account_page)

driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/ul/li[1]/a').click()

last_login = driver.find_element(By.XPATH, '//*[@id="licenses"]/div[2]/div/table/tbody/tr[7]/td[2]').text

print('__________________________________________________________')echo "# Unlocktool_change_pwd" >> README.md
print(f"Последний логин был:  {last_login}")
print(f"Новый пароль -  {new_password}")

time.sleep(10)

driver.quit