import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import LoginTest
# from LoginTest import driver

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

inputEmail.send_keys('julia@mail.com')
inputSenha.send_keys('1234')


inputEmail.send_keys(Keys.RETURN)

time.sleep(3)
botaoProdutos = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'nav a[href="/produto"]'))
)
botaoProdutos.click()

time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
time.sleep(2)

botaoSabonete = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="produtos"]/li[8]/a/img'))
)

botaoSabonete.click()

time.sleep(3)

inputQtd = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, '#quant-text'))
)

inputQtd.clear()
time.sleep(0.25)
inputQtd.send_keys('100000')

time.sleep(2)
botaoAdd = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div/div[2]/button'))
)
botaoAdd.click()

time.sleep(1)
driver.get("http://localhost:1337/finalizar")

time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

time.sleep(3)
botaoFinalizar = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div[7]/button'))
)

time.sleep(5)
driver.close()