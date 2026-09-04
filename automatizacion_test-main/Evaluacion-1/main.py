from tests import prueba5, prueba7, prueba8, prueba1, prueba2, prueba3, prueba6, prueba9, prueba4


def run_tests(tests):
    results = []

    for t in tests:
        try:
            print(f"Ejecutando test: {t.__name__}")
            s, m = t.run()
            results.append((t, s, m))
            print(f"Resultado: {'Exitoso ✅' if s else 'Fallido ❌'} - {m}")
        except Exception as e:
            results.append((t, False, f"Ha ocurrido un error durante la ejecución: {e}"))

    return results

if __name__ == "__main__":
    tests = [prueba1, prueba2, prueba3, prueba4, prueba5, prueba6, prueba7, prueba8, prueba9]
    results = run_tests(tests)

    print("\n\nResultados de los tests:")
    for test, successful, msg in results:
        print(f"Test: {test.__name__}: {'Exitoso ✅' if successful else 'Fallido ❌'} - {msg}")