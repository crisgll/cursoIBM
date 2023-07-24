def prueba_final():
    import random
    while True:
        try:
            n = int(input("Introduce el tamaño de matriz que deseas: "))#Tamaño matriz
            if type(n) is int:
                if n<=0:
                    print("El valor no es correcto, por favor introduce un número entero positivo")
                    continue
                else:
                    break
        except ValueError:
            print("Por favor, introduce un número entero positivo")
        except:
            print("Algo ha salido mal")
    matriz = []                                                 #Se inicializa la matriz vacía
    for i in range(n):                                          #Bucle for que recorrerá filas
        fila = []                                               #Inicializamos fila vacía
        for j in range(n):                                      #Bucle que recorre columnas
            fila.append(random.randint(0,9))                    #Valor aleatorio entero entre 0 y 9
        matriz.append(fila)                                     #Se añade el vector como fila en la matriz
    print("La matriz es:", matriz)                              #Se imprime la matriz en pantalla
    valor_fila = []                                             #Vectores donde se alojaran los valores sumas de filas y columnas
    valor_col = []
    for i in range(n):                                          #Bucle que recorre filas/columnas (mqtriz cuadrada)
        suma_fila = 0                                           #Variable contar las sumas de valores filas y columnas
        suma_col = 0
        for j in range(n):                                      #Bucle que recorre columnas/filas
            suma_fila = suma_fila + matriz[i][j]                #Se recorre dentro de la fila i cada valor en columna j, añadiéndose al valor obtenido en la columna j-1
            suma_col = suma_col + matriz[j][i]                  #Se recorre dentro de la columna i cada valor de la fila j, añadiéndose al obtenido en la fila j-1
        valor_fila.append(suma_fila)                            #Se añade al vector de valores de filas lo obtenido en el anterior bucle anidado
        valor_col.append(suma_col)                              #Se añade al vector de valores de columnas lo obtenido en bucle anterior
    print("Las sumas de cada fila son:", valor_fila)            #Se imprime por pantalla el vector con valores de suma de filas
    print("Las sumas de cada columna son:", valor_col)          #Se imprime por pantalla el vector con valores de suma de columnas
    return matriz

prueba_final()