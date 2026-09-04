from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Abre el navegador y navega hasta la página web
driver = webdriver.Chrome()
driver.get("https://www.recorrido.cl/es")

# Encuentra el botón "Mi Cuenta" utilizando el XPath correcto
mi_cuenta_button = driver.find_element(By.XPATH, '//*[@id="login-toggle"]')
mi_cuenta_button.click()

# Encuentra la pestaña "Iniciar Sesión"
iniciar_sesion_tab = driver.find_element(By.XPATH, '//*[@id="signin-tab"]')
iniciar_sesion_tab.click()

# Encuentra el enlace "Olvidé mi contraseña"
olvide_contrasena_link = driver.find_element(By.XPATH, '//*[@id="new_session"]/div[2]/div[3]/div[2]/a')
olvide_contrasena_link.click()

# Ejecuta JavaScript para hacer clic en el campo de texto para el correo electrónico
driver.execute_script("document.querySelector('#forgot_password_email').click();")

# Establece el valor del campo de texto usando JavaScript
driver.execute_script("document.querySelector('#forgot_password_email').value = 'fhlbkblgfaiapsoddc@hthlm.com';")

# Haz clic en el campo de texto identificado por el XPath y rellénalo con el correo electrónico
try:
    # Espera a que el campo esté presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#new_user_email'))
    )
    
    # Usar JavaScript para hacer clic en el campo de texto y rellenarlo con el correo electrónico
    driver.execute_script("document.querySelector('#new_user_email').click();")
    driver.execute_script("document.querySelector('#new_user_email').value = 'fhlbkblgfaiapsoddc@hthlm.com';")
except Exception as e:
    print(f"Error: {e}")

# Ejecuta JavaScript para hacer clic en el botón de envío
driver.execute_script("document.querySelector('#new_password > div.form-actions > input').click();")

try:
    # Campo de nueva contraseña
    new_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="new_user_password"]'))
    )
    # Campo de confirmación de contraseña
    confirm_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="new_user_password_confirmation"]'))
    )
    
    # Usar JavaScript para establecer el valor de ambos campos de contraseña
    driver.execute_script("arguments[0].value = 'clavenoesfalsa123';", new_password)
    driver.execute_script("arguments[0].value = 'clavenoesfalsa123';", confirm_password)
    
    # Verificar si los valores se han ingresado correctamente (opcional)
    print("Nueva contraseña:", driver.execute_script("return arguments[0].value;", new_password))
    print("Confirmación de contraseña:", driver.execute_script("return arguments[0].value;", confirm_password))
    
except Exception as e:
    print(f"Error: {e}")

# Pausa el script para que la página permanezca abierta
input("El campo de texto ha sido actualizado y el botón de envío ha sido clickeado. Presiona Enter para cerrar el navegador...")

# Cierra el navegador
driver.quit()
