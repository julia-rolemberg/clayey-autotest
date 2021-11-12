import LoginTest
from LoginTest import driver, EC, Keys, By, WebDriverWait, time
from selenium.webdriver.common.alert import Alert

driver.get('http://localhost:1337/pedido/listar')

botaoExcluir = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="paginaR"]/div[1]/table/tbody/tr/td[6]/button'))
)
botaoExcluir.click()

time.sleep(2)

# Aceita o alerta que confirma a exclusao
Alert(driver).accept()

time.sleep(0.5)
# Alerta de sucesso
Alert(driver).accept()

time.sleep(4)
driver.close()