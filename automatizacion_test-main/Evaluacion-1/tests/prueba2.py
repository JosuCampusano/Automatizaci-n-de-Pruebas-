#prueba 2 Genaro
#Login con datos vacíos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def run():
    # Configuración del WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Given: que puedo acceder a la aplicación
        driver.get("https://www.recorrido.cl/es")  # URL de la página principal

        # Pausa para ver la página cargada
        time.sleep(1)

        # When: puedo acceder al login
        login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
        login_link.click()

        login_lin = driver.find_element(By.XPATH, '//*[@id="signin-tab"]')
        login_lin.click()

        time.sleep(1)  # Esperar a que la página de login cargue completamente

        # And: ingreso con usuario vacío
        email_field = driver.find_element(By.XPATH, '//*[@id="user_email"]')
        email_field.clear()

        # And: ingreso con clave vacía
        password_field = driver.find_element(By.XPATH, '//*[@id="user_password"]')
        password_field.clear()
        time.sleep(1)

        # And: realizo el envío de los datos
        login_button = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/ul[2]/li[3]/div/div[2]/div/div/div[1]/div/div/div[1]/form/div[3]/input')
        login_button.click()

        # Then: se inicia sesión y redirecciona al dashboard
        time.sleep(3)  # Esperar a que se complete la redirección

        # Verificar que la URL es la del dashboard
        assert "https://www.recorrido.cl/users/sign_in?locale=es" in driver.current_url, "La URL no es la esperada"

        # Y aparece un mensaje de error "Email o contraseña inválidos."
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Email o contraseña inválidos.')]")

        if error_message.text != "Email o contraseña inválidos.":
            return False, f"El mensaje de error no es el esperado. Retornado: {error_message.text}."

        return True, "Test completado exitosamente."

    finally:
        # Cerrar el navegador
        driver.quit()
