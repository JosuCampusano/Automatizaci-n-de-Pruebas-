Feature: Búsqueda de Pasajes

  Scenario: Buscar un pasaje desde Santiago a La Serena para el día de mañana
    Given que puedo acceder a la aplicación
    When la página principal ha cargado
    And ingreso la ciudad de partida "Santiago"
    And ingreso la ciudad de llegada "La Serena"
    And ingreso la fecha de ida como mañana
    And hago clic en el botón de "Buscar"
    Then se abre una nueva pestaña con los viajes disponibles

  Scenario: Intentar seleccionar una fecha inválida
    Given que puedo acceder a la aplicación
    When la página principal ha cargado
    And presiono el campo de fecha de ida
    And escribo una fecha menor a hoy "30/08/2020"
    Then no se permite seleccionar un día anterior a hoy

