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

inputEmail.send_keys('julia@mail.com')
inputSenha.send_keys('1234')


inputEmail.send_keys(Keys.RETURN)

botaoCatalogo = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'nav a[href="/produto"]'))
)
botaoCatalogo.click()

time.sleep(2)
driver.execute_script("window.scrollTo(0, 600)")

time.sleep(2)

produto = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'img.card-img-top'))
)
produto.click()
time.sleep(2)

botaoAddCarrinho = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'button.add-to-cart'))
)
botaoAddCarrinho.click()


botaoFinalizarCarrinho = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'btnPedido'))
)
botaoFinalizarCarrinho.click()


botaoConcluir = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div[7]/button'))
)

botaoConcluir.click()


time.sleep(5)
driver.close()