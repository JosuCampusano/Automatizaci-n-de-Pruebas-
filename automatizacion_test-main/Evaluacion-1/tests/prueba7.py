from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, TimeoutException

def check(driver, timeout=10):
    try:
        # Esperar a que cualquier mensaje de error esté presente
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Contraseñas')]"))
        )
        
        # Buscar todos los mensajes que contienen la palabra "Contraseñas"
        error_messages = driver.find_elements(By.XPATH, "//*[contains(text(), 'Contraseñas')]")

        # Verificar si alguno de los mensajes contiene el texto exacto "Contraseñas no coinciden"
        for msg in error_messages:
            if "Contraseñas no coinciden" in msg.text:
                return True, "Contraseña no es igual."

        return False, "Error, mensaje de respuesta incorrecto o no encontrado."
    
    except (InvalidSelectorException, NoSuchElementException, TimeoutException) as e:
        return False, f"Error al buscar el mensaje: {e}"

def run():
    # Configuración del WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Acceder a la página principal
        driver.get("https://www.recorrido.cl/es")

        # Navegar a la página de registro
        login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
        login_link.click()
        time.sleep(3)

        # Ingresar un correo electrónico válido
        email_field = driver.find_element(By.XPATH, '//*[@id="new_user_email"]')
        email_field.clear()
        email_field.send_keys("rekaw8716@amxyy.com")

        # Ingresar una contraseña inválida
        password_field = driver.find_element(By.XPATH, '//*[@id="new_user_password"]')
        password_field.clear()
        password_field.send_keys("Clave12334")

        # Confirmar la contraseña (distinta a la anterior)
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

        time.sleep(5)

        successful, msg = check(driver, timeout=5)

        if not successful:
            return False, msg

        return True, "Test completado exitosamente: Mensaje de éxito mostrado."

    finally:
        # Cerrar el navegador
        driver.quit()


