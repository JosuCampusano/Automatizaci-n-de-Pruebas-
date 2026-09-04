# prueba 3 Genaro 
# Login con usuario correcto y password incorrecto
from selenium import webdriver
from selenium.webdriver.common.by import By
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

        # When: puedo acceder al login usando el "toggle login"
        toggle_login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
        toggle_login_link.click()

        # Acceder al login después de abrir el toggle
        login_link = driver.find_element(By.XPATH, '//*[@id="signin-tab"]')
        login_link.click()

        time.sleep(1)  # Esperar a que la página de login cargue completamente

        # And: ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com" (10 minuteMail)
        email_field = driver.find_element(By.XPATH, '//*[@id="user_email"]')
        email_field.clear()
        email_field.send_keys("fhlbkblgfaiapsoddc@hthlm.com")
        time.sleep(1)

        # And: ingreso una clave incorrecta "clavefalsa123"
        password_field = driver.find_element(By.XPATH, '//*[@id="user_password"]')
        password_field.clear()
        password_field.send_keys("clavefalsa123")
        time.sleep(1)

        # And: realizo el envío de los datos
        login_button = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/ul[2]/li[3]/div/div[2]/div/div/div[1]/div/div/div[1]/form/div[3]/input')
        login_button.click()

        # Then: redirecciona a https://www.recorrido.cl/users/sign_in?locale=es
        time.sleep(3)  # Esperar a que se complete la redirección
        assert "https://www.recorrido.cl/users/sign_in?locale=es" in driver.current_url, "No se redireccionó a la URL esperada"

        # Y aparece un mensaje de error "Email o contraseña inválidos."
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Email o contraseña inválidos.')]")

        if error_message.text != "Email o contraseña inválidos.":
            return False, f"El mensaje de error no es el esperado. Retornado: {error_message.text}."

        return True, "Test completado exitosamente: Mensaje de error mostrado y redirección correcta."

    finally:
        # Cerrar el navegador
        driver.quit()
