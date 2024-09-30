def sumatoria_promedio():
    n = 1
    lista_numero = []
    while n != 0:
        n = float(input('Ingresa un número o 0 (cero) para salir: '))
        if(n != 0):
            lista_numero.append(n)
            print(lista_numero)
        elif(n == 0):
            suma = sum(lista_numero)
            promedio =  suma / len(lista_numero)
            print()
            print(f'La sumatoria es: {round(suma, 2)}')
            print(f'Su promedio es: {round(promedio, 2)}')
            print('Fin del programa_')


sumatoria_promedio()
