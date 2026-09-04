from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time

def run():
    # Configuración del WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Given: que puedo acceder a la aplicación
        driver.get("https://www.recorrido.cl/es")  # URL de la página principal

        # Pausa para ver la página cargada
        time.sleep(2)

        # When: Página principal carga
        # And: ingreso Ciudad de partida "Santiago"
        departure_city = driver.find_element(By.XPATH, '//*[@id="bus_travel_departure_city_id-selectized"]')
        departure_city.clear()
        departure_city.send_keys("Santiago")
        departure_city.send_keys(Keys.ENTER)  # Simular presionar Enter para seleccionar la primera opción
        time.sleep(2)  # Pausa para esperar que cargue la lista desplegable

        # And: ingreso Ciudad de llegada "La Serena"
        arrival_city = driver.find_element(By.XPATH, '//*[@id="bus_travel_destination_city_id-selectized"]')
        arrival_city.clear()
        arrival_city.send_keys("La Serena")
        time.sleep(2)  # Pausa para esperar que cargue la lista desplegable
        arrival_city.send_keys(Keys.ENTER)  # Simular presionar Enter para seleccionar la primera opción

        # And: ingreso fecha de ida <Fecha Actual> - 1 día
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%d-%m-%Y")
        departure_date = driver.find_element(By.XPATH, '//*[@id="bus_travel_departure_date"]')
        time.sleep(1)
        departure_date.clear()
        departure_date.send_keys(yesterday)
        time.sleep(2)

        # And: hago clic en el botón de "Buscar"
        search_button = driver.find_element(By.XPATH, '//*[@id="bus-search-submit"]')
        search_button.click()
        time.sleep(2)

        # Then: Verifico que el campo de fecha de ida ha sido vaciado
        if departure_date.get_attribute('value') != "":
            return False, f"El campo de fecha no fue vaciado correctamente. Valor actual: {departure_date.get_attribute('value')}"

        return True, "Test completado exitosamente: El campo de fecha fue vaciado al ingresar una fecha inválida."

    finally:
        # Cerrar el navegador
        driver.quit()
