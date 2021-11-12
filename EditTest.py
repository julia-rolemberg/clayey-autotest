import LoginTest
from LoginTest import driver, EC, Keys, By, WebDriverWait, time

driver.get('http://localhost:1337/produto/listar')

botaoEditar = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/produto/alterar/1"]'))
)
botaoEditar.click()

time.sleep(2)

inputPreco = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.ID, 'valor_produto'))
)

inputPreco.clear()

inputPreco.send_keys(Keys.RETURN)


time.sleep(5)
driver.close()