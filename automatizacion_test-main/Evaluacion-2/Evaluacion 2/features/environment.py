# features/environment.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)

def before_all(context):
    logging.info("Configurando el WebDriver antes de todas las pruebas")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")  # Opcional: Ejecutar en modo headless

    # Especificar la ruta del ejecutable de Chrome si está en una ubicación no estándar
    # Descomenta y ajusta la línea siguiente si es necesario
    # chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Ajusta la ruta según tu instalación

    try:
        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    except Exception as e:
        logging.error(f"Error al inicializar Chrome WebDriver: {e}")
        raise

def after_all(context):
    logging.info("Cerrando el WebDriver después de todas las pruebas")
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    logging.info(f"Iniciando el escenario: {scenario.name}")

def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Reemplaza los caracteres no permitidos en nombres de archivos
        sanitized_name = "".join([c if c.isalnum() else "_" for c in scenario.name])
        screenshot_name = f"failed_scenario_{sanitized_name}.png"
        context.driver.save_screenshot(screenshot_name)
        logging.info(f"Escenario fallido. Captura de pantalla guardada como {screenshot_name}")
    logging.info(f"Finalizando el escenario: {scenario.name}")
