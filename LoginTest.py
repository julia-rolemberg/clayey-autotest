import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://localhost:1337/')

time.sleep(5)

iconeLogin = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'iconeUsuario'))
)
iconeLogin.click()

inputEmail = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'email'))
)
inputSenha = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'senha'))
)

inputEmail.send_keys('admin')
inputSenha.send_keys('1234')
inputEmail.send_keys(Keys.RETURN)


time.sleep(5)
driver.close()
