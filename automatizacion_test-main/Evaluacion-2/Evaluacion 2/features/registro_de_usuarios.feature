Feature: Registro de Usuarios

  Scenario: Registrar un usuario con datos válidos
    Given que puedo acceder a la aplicación
    When navego a la página de registro
    And ingreso un correo electrónico válido "rekaw87146@amxyy.com"
    And ingreso una contraseña válida "Clave1234"
    And confirmo la contraseña "Clave1234"
    And valido el captcha
    And hago clic en el botón de "Registrarse"
    Then se crea la cuenta y se envía un correo para activarla

  Scenario: Registro de usuarios sin correo
    Given que puedo acceder a la aplicación
    When navego a la página de registro
    And dejo sin dato el campo de correo electrónico
    And ingreso una contraseña válida "Clave1234"
    And confirmo la contraseña "Clave1234"
    And valido el captcha
    And hago clic en el botón de "Registrarse"
    Then no se crea la cuenta y se muestra el mensaje "Correo electrónico es requerido"

  Scenario: Registro de usuarios con contraseñas que no coinciden
    Given que puedo acceder a la aplicación
    When navego a la página de registro
    And ingreso un correo electrónico válido "rekaw87146@amxyy.com"
    And ingreso una contraseña válida "Clave1234"
    And confirmo la contraseña "Clave12345"
    And valido el captcha
    And hago clic en el botón de "Registrarse"
    Then no se crea la cuenta y se muestra el mensaje "Contraseñas no coinciden"
