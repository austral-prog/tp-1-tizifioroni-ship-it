def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas = total_segundos / 60 / 60
    minutos = (total_segundos / 60) % 60
    segundos_restantes = total_segundos % 60


    print (round(horas))
    print (round(minutos))
    print(segundos_restantes)

