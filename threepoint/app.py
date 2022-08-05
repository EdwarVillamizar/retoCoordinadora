import random
import sqlite3

def database():

    conexion=sqlite3.connect("arcade.db")

    try:
        conexion.execute("""create table gamer (
                                id integer primary key autoincrement,
                                name text,
                                score text
                            )""")
        print("se creo la tabla gamer")                        
    except sqlite3.OperationalError:
        print("La tabla gamer ya existe")                    
    conexion.close()

def opcionUno():

    print(end= "\n")

    print ("1. Piedra Papel Tijera")
    print ("2. Registro del jugador.")
    print ("3. Almacenamiento del puntaje del jugador")

    print ("4. Regresar")

    print(end= "\n")
    option = input('Ingrese Opcion: ')
    print(end= "\n")

    if option == "1": primerJuego()
    if option == "2": pass
    if option == "3": pass
    

def opcionDos():

    print(end= "\n")
    option = input('Ingrese nombre de jugador: ')
    print(end= "\n")

    if option:

        conexion=sqlite3.connect("arcade.db")
        conexion.execute("insert into gamer(name,score) values (?,?)", (option,0))
        conexion.commit()
        conexion.close()

    else:
        print("Ingrese nombre valido")


def opcionTres():

    lst = list()

    conexion=sqlite3.connect("arcade.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM gamer")
    
    rows = cursor.fetchall()

    print(end= "\n")
    print(end= "\n")
    print ("Seleccione Jugador")
    print(end= "\n")

    for row in rows:

        lst.append(str(row[0]))
        print("{}. Jugador: {}, Score: {}".format(row[0],row[1],row[2]))

    conexion.close()

    while True:
        print(end= "\n")
        option = input('Selecione id: ')
        print(end= "\n")
        if option in lst:
            break
        else:
            print("El jugador no existe")
            print(end= "\n")
    
    return option
        

def primerJuego():
    
    aleatorio = random.randrange(0, 3)
    elijePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Que elijes: "))

    if opcion == 1:
        elijeUsuario = "piedra"
    elif opcion == 2:
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Tu elijes: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "piedra"
    elif aleatorio == 1:
        elijePc = "papel"
    elif aleatorio == 2:
        elijePc = "tijera"
    print("PC elijio: ", elijePc)
    print("...")

    if elijePc == "piedra" and elijeUsuario == "papel":
        print("Ganaste, papel envulve piedra")
    elif elijePc == "papel" and elijeUsuario == "tijera":
        print("Ganaste, Tijera corta papel")
    elif elijePc == "tijera" and elijeUsuario == "piedra":
        print("Ganaste, Piedra pisa tijera")
    if elijePc == "papel" and elijeUsuario == "piedra":
        print("Perdiste, papel envulve piedra")
    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("Perdiste, Tijera corta papel")
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("Perdiste, Piedra pisa tijera")
    elif elijePc == elijeUsuario:
        print("Empate")

    conexion=sqlite3.connect("arcade.db")
    conexion.execute("insert into gamer(score) values (?,?)", (option,0))
    conexion.commit()
    conexion.close()

if __name__ == "__main__":

    database()
    
    id = opcionTres()

    while True:

        print(end= "\n")

        print ("1. Selección del juego.")
        print ("2. Registro del jugador.")
        print ("3. Almacenamiento del puntaje del jugador")
        print ("4. Control de intentos máximos")
        print ("5. Ranking de Jugadores con mejor puntaje")
        print ("6. Salir")

        print(end= "\n")
        option = input('Ingrese Opcion: ')
        print(end= "\n")

        if option == "1": opcionUno()
        if option == "2": opcionDos()
        if option == "3": opcionTres()
        if option == "4": pass
        if option == "5": pass
        if option == "6": break

