Feature: Control de Acceso

  Scenario: Login con datos correctos
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com"
    And ingreso una clave correcta "clavenoesfalsa123"
    And realizo el envío de los datos
    Then se inicia sesión y redirecciona al dashboard y muestra un mensaje de "Has iniciado sesión"

  Scenario: Login con datos vacíos
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And dejo el campo de usuario vacío
    And dejo el campo de clave vacío
    And realizo el envío de los datos
    Then redirecciona a la página de inicio de sesión y aparece un mensaje de error "Email o contraseña inválidos."

  Scenario: Login con usuario correcto y password incorrecto
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com"
    And ingreso una clave incorrecta "clavefalsa123"
    And realizo el envío de los datos
    Then redirecciona a la página de inicio de sesión y aparece un mensaje de error "Email o contraseña inválidos."

  Scenario: Login con usuario incorrecto y password correcto
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And ingreso como usuario "usuarioFalso@algo.cl"
    And ingreso una clave correcta "clavenoesfalsa123"
    And realizo el envío de los datos
    Then redirecciona a la página de inicio de sesión y aparece un mensaje de error "Email o contraseña inválidos."
