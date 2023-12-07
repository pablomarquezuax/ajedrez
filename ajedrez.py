# Función principal, guarda los tableros de cada movimiento en un archivo .txt
def guardar_tableros(nombre_fichero):

    # Representamos un tablero como una cadena separando las filas por cambios de línea y las columnas por tabuladores.
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    
    # Para que el jugador pueda elegir el nombre del fichero con los tableros de su partida
    nombre_fichero = input("Ingrese el nombre del archivo para guardar el tablero inicial: ")

    # Lista vacía (tablero) donde se puedan ir guardando las filas nuevas
    tablero =  []

    # Bucle que recorre las filas del tablero inicial
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))


    # Se abre el fichero con 'w' para que se pueda escibir
    f = open(nombre_fichero, 'w')


    # Este bucle recorre todas las filas del tablero ('i' va tomando el valor de cada fila)
    for i in tablero:
        # Va uniendo las fichas de cada fila, separadas por tabuladores
        f.write('\t'.join(i) + '\n')


    # Cerramos el fichero.
    f.close()


    # Contador de movimientos (al iniciar la partida esta siempre en 0)
    movimientos = 0


    # Bucle para jugar la partida hasta que el usario decida terminar.
    while True:

        # Preguntamos al usuario si quiere seguir jugando (realizar más movimientos).
        continuar = input('Deseas hacer otro movimiento (s/n): ')

        # Comprobamos si el jugador ha constestado que si
        if continuar != 's':

            # Si el usuario no ha contestado que si, termina la partida.
            break

        else:
            # Para hacer un movimiento hay que indicar las coordenadas de origen y destino de la ficha que se prentende mover
            fila_origen = int(input('Introduce la fila de la pieza a mover: '))
            columna_origen = int(input('Introduce la columna de la pieza a mover: '))
            fila_destino = int(input('Introduce la fila de destino: '))
            columna_destino = int(input('Introduce la columna de destino: '))


            # Se hace el movimiento indicado por el jugador
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_origen-1][columna_origen-1]
            # Cambiamos las posición inicial de la ficha por un espacio en blanco
            tablero[fila_origen-1][columna_origen-1] = ''


            # Incrementamos el contador de movimientos en 1.
            movimientos += 1


            # Abrimos el fichero en modo añadir ('a').
            f = open(nombre_fichero, 'a')

            # Añadimos el número de movimiento.
            f.write('Movimiento' + str(movimientos) + '\n')


            # Este bucle recorre todas las filas del tablero ('i' va tomando el valor de cada fila)
            for i in tablero:
                 # Va uniendo las fichas de cada fila, separadas por tabuladores
                f.write('\t'.join(i) + '\n')


            # Cerramos el fichero.
            f.close()


        # Preguntamos al usuario si quiere ver el tablero en algún movimiento específico.
        ver_tablero = input('¿Quieres ver el tablero en algún movimiento específico? (s/n): ')
        if ver_tablero == 's':
            # Solicitamos al jugador el número de movimiento que desea ver.
            num_movimiento = int(input('Introduce el número de movimiento que quieres ver: '))

            # Abrimos el fichero en modo lectura.
            with open(nombre_fichero, 'r') as f:
                # Leemos todas las líneas del fichero.
                lineas = f.readlines()

                # Buscamos la línea que contiene el tablero del movimiento solicitado.
                inicio_tablero = lineas.index(f'Movimiento{num_movimiento}\n') + 1
                fin_tablero = inicio_tablero + 8  # Suponemos que el tablero ocupa 8 líneas.

                # Extraemos las líneas correspondientes al tablero.
                tablero_movimiento = [line.strip().split('\t') for line in lineas[inicio_tablero:fin_tablero]]

                # Mostramos el tablero por pantalla.
                mostrar_tablero(tablero_movimiento)

            
    return


def mostrar_tablero(tablero):
    # Bucle iterativo para recorrer las filas del tablero.
    for i in tablero:
        # Mostramos por pantalla cada fila concatenando los caracteres que contiene.
        print('\t'.join(i) + '\n')


guardar_tableros('partida1.txt')