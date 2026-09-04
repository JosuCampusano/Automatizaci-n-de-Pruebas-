# prueba 9 Matias - Buscar un Pasaje desde Santiago a La Serena para el día de mañana
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

        # And: ingreso fecha de ida <Fecha Actual> + 1 día
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")
        tomorrow_url_format = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")  # Fecha dinámica
        departure_date = driver.find_element(By.XPATH, '//*[@id="bus_travel_departure_date"]')
        time.sleep(1)
        departure_date.clear()
        departure_date.send_keys(tomorrow)
        time.sleep(5)

        # And: hago clic en el botón de "Buscar"
        search_button = driver.find_element(By.XPATH, '//*[@id="bus-search-submit"]')
        search_button.click()

        # Then: Abre una nueva pestaña con los viajes disponibles
        time.sleep(12)  # Esperar a que se cargue la nueva página con los resultados de los viajes

            # Obtener todas las pestañas abiertas
        windows = driver.window_handles

        # Cerrar la primera pestaña (principal)
        driver.switch_to.window(windows[0])
        driver.close()

        # Cambiar el control a la nueva pestaña (resultados de búsqueda)
        driver.switch_to.window(windows[1])

        # Verificar que la URL contiene los parámetros de búsqueda y la nueva página ha sido cargada
        if driver.current_url != f"https://www.recorrido.cl/es/bus/santiago/la-serena/{tomorrow_url_format}":
            return False, f"La URL de resultados no se cargó correctamente. URL actual: {driver.current_url}"

        return True, f"Test completado exitosamente: Se encontraron resultados de viajes para el día {tomorrow}."

    finally:
        # Cerrar el navegador
        driver.quit()
