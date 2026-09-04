Feature: Cierre de Sesión

  Scenario: Cerrar sesión de forma segura
    Given que estoy en la aplicación y he iniciado sesión
    When hago clic en el botón de "Cerrar sesión"
    Then soy redirigido a la página de inicio y mi sesión se cierra correctamente
