#Creación de matriz NxN
def prueba_final():                                             # El usuario debe aportar el valor N, que será el tamaño de la matriz
    import random
    try:
        N = int(input("Introduce el tamaño de matriz que deseas: "))# Se pide al usuario que introduzca un tamaño para la matriz
    except ValueError:
        print("El valor introducido no es compatible")
    except:
        print("Algo ha salido mal")
    matriz = []                                                 # Se inicializa la matriz vacía
    for i in range(N):                                          # Bucle for que recorrerá filas
        fila = []                                               # Inicializamos fila vacía
        for j in range(N):                                      # Bucle que recorre columnas
            fila.append(random.randint(0,9))                    # Añadimos un valor aleatorio entero entre 0 y 9 a la columna de la fila (vector) que estamos tratando
        matriz.append(fila)                                     # Se añade el vector calculado anteriormente como fila en la matriz
    print("La matriz es:", matriz)                              # Se imprime la matriz en pantalla
    valor_fila = []                                             # Inicializamos los vectores donde se alojaran los valores de la suma de filas y columnas
    valor_col = []
    for i in range(N):                                          # Bucle que recorre filas/columnas, en este caso al ser matrices cuadradas no es necesario distinguir casos para filas y columnas, y se puede calcular a la vez
        suma_fila = 0                                           # Variable para contar las sumas de valores de cada fila y columna
        suma_col = 0
        for j in range(N):                                      # Bucle que recorre columnas/filas
            suma_fila = suma_fila + matriz[i][j]                # Se recorre dentro de la fila i cada valor en columna j, añadiéndose al valor obtenido en la columna j-1
            suma_col = suma_col + matriz[j][i]                  # Se recorre dentro de la columna i cada valor de la fila j, añadiéndose al obtenido en la fila j-1
        valor_fila.append(suma_fila)                            # Se añade al vector de valores de filas lo obtenido en el anterior bucle anidado
        valor_col.append(suma_col)                              # Se añade al vector de valores de columnas lo obtenido en bucle anterior
    print("Las sumas de cada fila son:", valor_fila)            # Se imprime por pantalla el vector con valores de suma de filas
    print("Las sumas de cada columna son:", valor_col)          # Se imprime por pantalla el vector con valores de suma de columnas
    return matriz

prueba_final()