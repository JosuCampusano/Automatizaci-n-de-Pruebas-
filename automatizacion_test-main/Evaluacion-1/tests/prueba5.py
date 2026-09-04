from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, TimeoutException

def check(driver, xpath_expression, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath_expression))
        )
        msg = driver.find_element(By.XPATH, xpath_expression).text

        if msg != "Te hemos enviado un email con instrucciones para que confirmes tu cuenta.":
            return False, f"Error, mensaje de respuesta incorrecto: {msg}"
        
        return True, "Cuenta creada satisfactoriamente."
    
    except (InvalidSelectorException, NoSuchElementException, TimeoutException) as e:
        return False, f"Error al buscar el mensaje: {e}"

def generar_string_aleatorio():
    return ''.join([str(random.randint(0, 12)) for _ in range(7)])

def run():
    # Configuración del WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Acceder a la página principal
        driver.get("https://www.recorrido.cl/es")

        # Navegar a la página de registro
        login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
        login_link.click()
        time.sleep(3)  # Esperar a que la página de registro cargue completamente

        # Ingresar un correo electrónico válido
        email = generar_string_aleatorio() + '@duoctest.cl'
        email_field = driver.find_element(By.XPATH, '//*[@id="new_user_email"]')
        email_field.clear()
        email_field.send_keys('hsdfhfhdsf@gmail.com')

        # Ingresar una contraseña válida
        password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password"]')
        password_field.clear()
        password_field.send_keys("Clave1234")

        # Confirmar la contraseña
        confirm_password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password_confirmation"]')
        confirm_password_field.clear()
        confirm_password_field.send_keys("Clave1234")

        # Esperar la intervención manual para el CAPTCHA
        input("Por favor, resuelve el CAPTCHA manualmente y presiona Enter para continuar...")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="signup"]/form/div[3]/input'))
        )

        register_button = driver.find_element(By.XPATH, '//*[@id="signup"]/form/div[3]/input')
        register_button.click()

        # Esperar a que se complete el proceso de registro
        time.sleep(5)

        successfull, msg = check(driver, '//*[@id="flash_notice"]', timeout=5)

        if not successfull:
            return False, msg

        return True, "Test completado exitosamente: Mensaje de éxito mostrado."
    finally:
        # Cerrar el navegador
        driver.quit()


