import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://localhost:1337/')

time.sleep(4)


botaoDescubra = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/quiz"]'))
)
botaoDescubra.click()

time.sleep(3)
# Scroll para o fim da pagina
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 


botaoComecar = WebDriverWait(driver, 20).until(
 	EC.presence_of_element_located((By.ID, 'start-btn'))
)

time.sleep(1)

botaoComecar.click()

time.sleep(2)

opcoes = ["Oleosa", "Esfoliação média", "Relaxamento", "Espumação leve", "100% natural"]
botaoProximo = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'next-btn'))
)
botaoFinalizar = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'final-btn'))
)

for alternativa in opcoes:
    
    botaoAlternativa = driver.find_element(By.XPATH, f"//*[contains(text(), '{alternativa}')]")
    driver.execute_script("window.scrollTo(0, 70)")
    time.sleep(2)
    botaoAlternativa.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1.5)
    try:
        botaoProximo.click()
    except:
        botaoFinalizar.click()
    time.sleep(2.5)

driver.execute_script("window.scrollTo(0, 50)") 
time.sleep(5)
botaoResultado = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'result-btn'))
    )
botaoResultado.click()

time.sleep(5)
driver.close()