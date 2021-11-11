import LoginTest
from LoginTest import driver, EC, Keys, By, WebDriverWait, time

driver.get('http://localhost:1337/produto/listar')

botaoEditar = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/produto/alterar/1"]'))
)
botaoEditar.click()

time.sleep(2)

inputPreco = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, '#valor_produto'))
)

inputPreco.send_keys(Keys.CLEAR)

time.sleep(2)
botaoSalvar = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '"//*[@id="form"]/div[11]/button"'))
)

time.sleep(1)
driver.execute_script("window.scrollTo(0, 0)")

time.sleep(5)
driver.close()