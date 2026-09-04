# features/steps/steps.py

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import logging
from datetime import datetime, timedelta

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# -----------------------------
# Definiciones de Pasos Generales
# -----------------------------

@given('que puedo acceder a la aplicación')
def step_impl(context):
    logging.info("Accediendo a la aplicación")
    context.driver.get("https://www.recorrido.cl/es")
    try:
        WebDriverWait(context.driver, 10).until(
            EC.title_contains("Recorrido")
        )
    except TimeoutException:
        context.driver.save_screenshot("error_pagina_principal.png")
        raise

@when('la página principal ha cargado')
def step_impl(context):
    logging.info("Verificando que la página principal ha cargado")
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except TimeoutException:
        context.driver.save_screenshot("error_pagina_principal_carga.png")
        raise

# -----------------------------
# Pasos para Control de Acceso
# -----------------------------

@when('puedo acceder al login')
def step_impl(context):
    logging.info("Navegando al formulario de login")
    try:
        login_toggle = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-toggle"))
        )
        login_toggle.click()
        signin_tab = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin-tab"))
        )
        signin_tab.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_acceder_login.png")
        raise

@when('ingreso como usuario "{email}"')
def step_impl(context, email):
    logging.info(f"Ingresando el usuario: {email}")
    try:
        email_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user_email"))
        )
        email_field.clear()
        email_field.send_keys(email)
        
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_usuario.png")
        raise

@when('ingreso una clave correcta "{password}"')
def step_impl(context, password):
    logging.info(f"Ingresando la clave correcta: {password}")
    try:
        password_field = context.driver.find_element(By.ID, "user_password")
        password_field.clear()
        password_field.send_keys(password)

    except NoSuchElementException:
        context.driver.save_screenshot("error_ingresar_clave.png")
        raise

@when('ingreso una clave incorrecta "{password}"')
def step_impl(context, password):
    logging.info(f"Ingresando la clave incorrecta: {password}")
    try:
        
        password_field = context.driver.find_element(By.ID, "user_password")
        password_field.clear()
        password_field.send_keys(password)
    except NoSuchElementException:
        context.driver.save_screenshot("error_ingresar_clave.png")
        raise

@when('dejo el campo de usuario vacío')
def step_impl(context):
    logging.info("Dejando el campo de usuario vacío")
    try:        
        email_field = context.driver.find_element(By.ID, "user_email")
        email_field.clear()
    except NoSuchElementException:
        context.driver.save_screenshot("error_campo_usuario_vacio.png")
        raise

@when('dejo el campo de clave vacío')
def step_impl(context):
    logging.info("Dejando el campo de clave vacío")
    try:
        password_field = context.driver.find_element(By.ID, "user_password")
        password_field.clear()


    except NoSuchElementException:
        context.driver.save_screenshot("error_campo_clave_vacio.png")
        raise

@when('realizo el envío de los datos')
def step_impl(context):
    logging.info("Realizando el envío de los datos de login")
    try:
        login_button = context.driver.find_element(By.XPATH, "//input[@value='Ingresar']")
        login_button.click()
    except NoSuchElementException:
        context.driver.save_screenshot("error_enviar_datos_login.png")
        raise

@then('se inicia sesión y redirecciona al dashboard y muestra un mensaje de "Has iniciado sesión"')
def step_impl(context):
    logging.info("Verificando que se haya iniciado sesión correctamente")
    try:
        WebDriverWait(context.driver, 10).until(
            EC.url_contains("/users/dashboard")
        )
        success_message = context.driver.find_element(By.CLASS_NAME, "notice")
        assert "Has iniciado sesión" in success_message.text, f"Mensaje inesperado: {success_message.text}"
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_iniciar_sesion.png")
        raise

@then('redirecciona a la página de inicio de sesión y aparece un mensaje de error "Email o contraseña inválidos."')
def step_impl(context):
    logging.info("Verificando mensaje de error por credenciales inválidas")
    try:
        WebDriverWait(context.driver, 10).until(
            EC.url_contains("/users/sign_in")
        )
        error_message = context.driver.find_element(By.CLASS_NAME, "error")
        assert "Email o contraseña inválidos" in error_message.text, f"Mensaje inesperado: {error_message.text}"
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_credenciales_invalidas.png")
        raise

# -----------------------------
# Pasos para Registro de Usuarios
# -----------------------------

@when('navego a la página de registro')
def step_impl(context):
    logging.info("Navegando a la página de registro")
    try:
        login_toggle = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-toggle"))
        )
        login_toggle.click()
        signup_tab = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signup-tab"))
        )
        signup_tab.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_navegar_registro.png")
        raise

@when('ingreso un correo electrónico válido "{email}"')
def step_impl(context, email):
    logging.info(f"Ingresando correo electrónico válido: {email}")
    try:
        email_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "new_user_email"))
        )
        email_field.clear()
        email_field.send_keys(email)
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_correo_valido.png")
        raise

@when('dejo sin dato el campo de correo electrónico')
def step_impl(context):
    logging.info("Dejando sin dato el campo de correo electrónico")
    try:
        email_field = context.driver.find_element(By.ID, "new_user_email")
        email_field.clear()
    except NoSuchElementException:
        context.driver.save_screenshot("error_campo_correo_vacio.png")
        raise

@when('ingreso una contraseña válida "{password}"')
def step_impl(context, password):
    logging.info(f"Ingresando contraseña válida: {password}")
    try:
        password_field = context.driver.find_element(By.ID, "new_user_password")
        password_field.clear()
        password_field.send_keys(password)
    except NoSuchElementException:
        context.driver.save_screenshot("error_ingresar_contrasena.png")
        raise

@when('confirmo la contraseña "{password_confirmation}"')
def step_impl(context, password_confirmation):
    logging.info(f"Confirmando contraseña: {password_confirmation}")
    try:
        confirm_field = context.driver.find_element(By.ID, "new_user_password_confirmation")
        confirm_field.clear()
        confirm_field.send_keys(password_confirmation)
    except NoSuchElementException:
        context.driver.save_screenshot("error_confirmar_contrasena.png")
        raise

@when('valido el captcha')
def step_impl(context):
    logging.info("Validando el captcha")
    # Captcha no automatizable. Debería ser deshabilitado en el entorno de pruebas.
    pass


@then('se crea la cuenta y se envía un correo para activarla')
def step_impl(context):
    logging.info("Verificando que se crea la cuenta y se envía un correo para activarla")
    try:
        success_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "notice"))
        )
        assert "Te hemos enviado un correo para activar tu cuenta" in success_message.text, f"Mensaje inesperado: {success_message.text}"
    except (TimeoutException, AssertionError):
        context.driver.save_screenshot("error_crear_cuenta.png")
        raise

@then('no se crea la cuenta y se muestra el mensaje "Correo electrónico es requerido"')
def step_impl(context):
    logging.info('Verificando mensaje de error "Correo electrónico es requerido"')
    try:
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Correo electrónico es requerido')]"))
        )
        assert error_message.is_displayed(), "El mensaje de error no se muestra"
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_correo_requerido.png")
        raise

@then('no se crea la cuenta y se muestra el mensaje "Contraseñas no coinciden"')
def step_impl(context):
    logging.info('Verificando mensaje de error "Contraseñas no coinciden"')
    try:
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Contraseñas no coinciden')]"))
        )
        assert error_message.is_displayed(), "El mensaje de error no se muestra"
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_contrasenas_no_coinciden.png")
        raise

# -----------------------------
# Pasos para Búsqueda de Pasajes
# -----------------------------

@when('ingreso la ciudad de partida "{ciudad_partida}"')
def step_impl(context, ciudad_partida):
    logging.info(f"Ingresando la ciudad de partida: {ciudad_partida}")
    try:
        partida_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "bus_travel_departure_city_id-selectized"))
        )
        partida_field.clear()
        partida_field.send_keys(ciudad_partida)
        partida_field.send_keys(Keys.RETURN)
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_ciudad_partida.png")
        raise

@when('ingreso la ciudad de llegada "{ciudad_llegada}"')
def step_impl(context, ciudad_llegada):
    logging.info(f"Ingresando la ciudad de llegada: {ciudad_llegada}")
    try:
        llegada_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "bus_travel_destination_city_id-selectized"))
        )
        llegada_field.clear()
        llegada_field.send_keys(ciudad_llegada)
        llegada_field.send_keys(Keys.RETURN)
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_ciudad_llegada.png")
        raise

@when('ingreso la fecha de ida como mañana')
def step_impl(context):
    logging.info("Ingresando la fecha de ida como mañana")
    try:
        fecha_ida = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        fecha_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "bus_travel_departure_date"))
        )
        fecha_field.clear()
        fecha_field.send_keys(fecha_ida)
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_fecha_ida.png")
        raise

@then('se abre una nueva pestaña con los viajes disponibles')
def step_impl(context):
    logging.info("Verificando que se abre una nueva pestaña con los viajes disponibles")
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1
        )
        context.driver.switch_to.window(context.driver.window_handles[-1])
        WebDriverWait(context.driver, 10).until(
            EC.title_contains("Recorrido")
        )
    except TimeoutException:
        context.driver.save_screenshot("error_nueva_pestana_viajes.png")
        raise

@when('presiono el campo de fecha de ida')
def step_impl(context):
    logging.info("Presionando el campo de fecha de ida")
    try:
        fecha_field = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bus_travel_departure_date"))
        )
        fecha_field.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_presionar_fecha_ida.png")
        raise

@when('escribo una fecha menor a hoy "{fecha}"')
def step_impl(context, fecha):
    logging.info(f"Ingresando una fecha menor a hoy: {fecha}")
    try:
        fecha_field = context.driver.find_element(By.ID, "bus_travel_departure_date")
        fecha_field.clear()
        fecha_field.send_keys(fecha)
    except NoSuchElementException:
        context.driver.save_screenshot("error_ingresar_fecha_invalida.png")
        raise

@then('no se permite seleccionar un día anterior a hoy')
def step_impl(context):
    logging.info("Verificando que no se permite seleccionar un día anterior a hoy y cerrando sesión")
    try:
        # Verificamos el mensaje de error
        mensaje_error = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'No puede seleccionar fecha menor a hoy')]"))
        )
        assert mensaje_error.is_displayed(), "El mensaje de error no se muestra"


        logging.info("Mensaje verificado y sesión cerrada correctamente")
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_fecha_anterior_hoy.png")
        raise AssertionError("Error al verificar el mensaje o cerrar la sesión")


# -----------------------------
# Pasos para Restablecimiento de Contraseñas
# -----------------------------

@when('navego a la página de inicio de sesión')
def step_impl(context):
    logging.info("Navegando a la página de inicio de sesión")
    try:
        login_toggle = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-toggle"))
        )
        login_toggle.click()
        signin_tab = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin-tab"))
        )
        signin_tab.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_navegar_inicio_sesion.png")
        raise

@when('selecciono la opción de "¿Olvidaste tu contraseña?"')
def step_impl(context):
    logging.info('Seleccionando la opción de "¿Olvidaste tu contraseña?"')
    try:
        forgot_password_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Olvidé mi contraseña"))
        )
        forgot_password_link.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_seleccionar_olvidaste_contrasena.png")
        raise

@when('ingreso un correo electrónico registrado "{email}"')
def step_impl(context, email):
    logging.info(f"Ingresando correo electrónico registrado: {email}")
    try:
        email_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "forgot_password_email"))
        )
        email_field.clear()
        email_field.send_keys(email)
        enviar = context.driver.find_element((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input"))
        enviar.click()
        

    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_correo_registrado.png")
        raise

@when('ingreso un correo electrónico no registrado "{email}"')
def step_impl(context, email):
    logging.info(f"Ingresando correo electrónico no registrado: {email}")
    try:
        email_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "forgot_password_email"))
        )
        email_field.clear()
        email_field.send_keys(email)
        enviar = context.driver.find_element((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input"))
        enviar.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot("error_ingresar_correo_no_registrado.png")
        raise

@then('recibo un mensaje de confirmación y se envía un correo con las instrucciones para restablecer mi contraseña')
def step_impl(context):
    logging.info("Verificando que se recibe un mensaje de confirmación")
    try:
        confirmation_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "notice"))
        )
        assert "Te hemos enviado un correo electrónico con las instrucciones para restablecer tu contraseña" in confirmation_message.text, f"Mensaje inesperado: {confirmation_message.text}"
    except (TimeoutException, AssertionError):
        context.driver.save_screenshot("error_confirmacion_recuperar_contrasena.png")
        raise

@then('aparece un mensaje de error indicando que el correo no está registrado')
def step_impl(context):
    logging.info("Verificando mensaje de error por correo no registrado")
    try:
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert "El correo no está registrado" in error_message.text, f"Mensaje inesperado: {error_message.text}"
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_correo_no_registrado.png")
        raise

# -----------------------------
# Pasos para Cierre de Sesión
# -----------------------------

@given('que estoy en la aplicación y he iniciado sesión')
def step_impl(context):
    logging.info("Iniciando sesión en la aplicación")
    # Implementar el inicio de sesión aquí
    context.execute_steps('''
        When puedo acceder al login
        And ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com"
        And ingreso una clave correcta "clavenoesfalsa123"
        And realizo el envío de los datos
    ''')

@then('soy redirigido a la página de inicio y mi sesión se cierra correctamente')
def step_impl(context):
    logging.info("Verificando que la sesión se cierra correctamente y se redirige a la página de inicio")
    try:
        WebDriverWait(context.driver, 10).until(
            EC.url_to_be("https://www.recorrido.cl/es")
        )
        # Verificar que el botón de login está visible, lo que indica que la sesión se ha cerrado
        login_toggle = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-toggle"))
        )
        assert login_toggle.is_displayed(), "El botón de login no está visible; la sesión podría no haberse cerrado correctamente"
    except (TimeoutException, NoSuchElementException, AssertionError):
        context.driver.save_screenshot("error_cerrar_sesion.png")
        raise

@when('cierro la sesión')
def step_impl(context):
    logging.info("Iniciando el proceso de cierre de sesión")
    try:    
                # Abrir el menú de usuario para acceder a "Salir"
        login_togglee = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-toggle"))
        )
        login_togglee.click()

        # Buscar y hacer clic en el enlace "Salir"
        logout_link = WebDriverWait(context.driver, 10).until(
             EC.element_to_be_clickable((By.LINK_TEXT, "Salir"))
        )
        logout_link.click()
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-toggle"))
        )
        logging.info("Cierre de sesión completado exitosamente")
    except (TimeoutException, NoSuchElementException) as e:
        context.driver.save_screenshot("error_cerrar_sesion.png")
        logging.error(f"Error al cerrar sesión: {e}")
        raise

# -----------------------------
# Definición Genérica para Clicar Botones
# -----------------------------

@when('hago clic en el botón de "{boton}"')
def step_impl(context, boton):
    logging.info(f"Haciendo clic en el botón de '{boton}'")
    try:
        boton_element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, f"//button[contains(text(), '{boton}')] | //input[@value='{boton}'] | //a[contains(text(), '{boton}')]"
            ))
        )
        boton_element.click()
    except (TimeoutException, NoSuchElementException):
        context.driver.save_screenshot(f"error_clic_boton_{boton}.png")
        raise

@then('el WebDriver está inicializado')
def step_impl(context):
    assert hasattr(context, 'driver'), "El WebDriver no está inicializado en el contexto"
