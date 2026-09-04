Feature: Restablecimiento de Contraseñas

  Scenario: Restablecer contraseña con correo válido
    Given que puedo acceder a la aplicación
    When navego a la página de inicio de sesión
    And selecciono la opción de "¿Olvidaste tu contraseña?"
    And ingreso un correo electrónico registrado "fhlbkblgfaiapsoddc@hthlm.com"
    And hago clic en el botón de "Enviar instrucciones"
    Then recibo un mensaje de confirmación y se envía un correo con las instrucciones para restablecer mi contraseña

  Scenario: Restablecer contraseña con correo no registrado
    Given que puedo acceder a la aplicación
    When navego a la página de inicio de sesión
    And selecciono la opción de "¿Olvidaste tu contraseña?"
    And ingreso un correo electrónico no registrado "correo_no_registrado@dominio.com"
    And hago clic en el botón de "Enviar instrucciones"
    Then aparece un mensaje de error indicando que el correo no está registrado

