# prueba 6 Genaro - Restablecer contraseña con correo válido

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Given: Dado que accedo a la aplicación y navego a la página de inicio de sesión
    driver.get("https://www.recorrido.cl/es")  # URL de la página principal
    time.sleep(1)

    # Acceder al login usando el "toggle login"
    toggle_login_link = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
    toggle_login_link.click()
    time.sleep(1)

    # Acceder al login después de abrir el toggle
    login_link = driver.find_element(By.XPATH, '//*[@id="signin-tab"]')
    login_link.click()
    time.sleep(1)  # Esperar a que la página de login cargue completamente

    # When: selecciono la opción de "¿Olvidaste tu contraseña?"
    forgot_password_link = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[2]/ul[2]/li[3]/div/div[2]/div/div/div[1]/div/div/div[1]/form/div[2]/div[3]/div[2]/a')
    forgot_password_link.click()
    time.sleep(1)

    # And: Ingreso un correo electrónico registrado: fhlbkblgfaiapsoddc@hthlm.com
    email_field = driver.find_element(By.XPATH, '//*[@id="forgot_password_email"]')
    email_field.clear()
    email_field.send_keys("fhlbkblgfaiapsoddc@hthlm.com")
    time.sleep(2)
    email_field.send_keys(Keys.ENTER)

    # Pausa para esperar el mensaje de confirmación
    time.sleep(3)

# Then: Verifico que se ha mostrado el mensaje de confirmación esperado
    confirmation_message_element = EC.presence_of_element_located((By.XPATH, '//*[@id="flash_notice"]'))
    confirmation_message_text = confirmation_message_element.text

    # Verificación personalizada
    if confirmation_message_text != "Recibirás un email con instrucciones para reiniciar tu contraseña en unos minutos.":
        print(f"Test fallido: El mensaje de confirmación no es correcto. Mensaje actual: {confirmation_message_text}")
    else:
        print("Test completado exitosamente: Mensaje de confirmación mostrado correctamente.")

finally:
    # Cerrar el navegador
    driver.quit()


#que bueno que hicimos esto, que bueno que no hicimos esto. que mal que no lo hicimos
