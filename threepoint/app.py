import random
import sqlite3

def database():

    conexion=sqlite3.connect("arcade.db")

    try:
        conexion.execute("""Create TABLE if not exists gamer (
                                id integer primary key autoincrement,
                                name text,
                                score text
                            )""")
        #print("se creo la tabla gamer")   
       
        conexion.commit()    

    except sqlite3.OperationalError:
        pass

    try:
        conexion.execute("""Create TABLE if not exists palabras(
                                id integer primary key autoincrement,
                                name text
                            )""")
        conexion.commit()  

    except sqlite3.OperationalError:
        pass

    palabras = ['lobo','perro','gato','zorro','loro']
    cursor = conexion.cursor()
    for item in palabras:
        cursor.execute("INSERT OR IGNORE INTO palabras(name) values (?)", (item,))
        conexion.commit()
    conexion.execute("INSERT OR IGNORE INTO gamer(id,name,score) values (?,?,?)", (1,"Player 1",0))
    conexion.commit() 

    conexion.close()

def opcionUno(id,life):

    print(end= "\n")

    print ("1. Piedra Papel Tijera.")
    print ("2. Ahorcado.")
    print ("3. Astucia Naval.")

    print(end= "\n")
    option = input('Ingrese Opcion: ')
    print(end= "\n")

    if option == "1": primerJuego(id)
    if option == "2": segundoJuego(id,life)
    if option == "3": tercerJuego()
    
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
    print ("Jugadores")
    print(end= "\n")

    for row in rows:

        lst.append(str(row[0]))
        print("{}. Jugador: {}, Score: {}".format(row[0],row[1],row[2]))

    conexion.close()

    while True:
        print(end= "\n")
        option = input('Seleccione id: ')
        print(end= "\n")
        if option in lst:
            break
        else:
            print("El jugador no existe")
            print(end= "\n")
    
    return option

def opcionCuatro(): 

    print(end= "\n")
    option = int(input('Ingrese numero de vidas: '))
    print(end= "\n")
    return option

def opcionCinco():

    conexion=sqlite3.connect("arcade.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM gamer ORDER BY score  DESC")
    
    rows = cursor.fetchall()

    print(end= "\n")
    print(end= "\n")
    print ("Ranking del mejor puntaje")
    print(end= "\n")

    for row in rows:

        print("{}. Jugador: {}, Score: {}".format(row[0],row[1],row[2]))
    
    print(end= "\n")
    conexion.close()
        
def primerJuego(id):
    
    print(end= "\n")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print(end= "\n")
    
    opcion = int(input("Que elijes: "))
    pc = random.randrange(0, 3)

    if opcion == 1:
        jugador = "piedra"
    elif opcion == 2:
        jugador = "papel"
    elif opcion == 3:
        jugador = "tijera"
    print("Tu elijes: ", jugador)

    if pc == 0:
        pc = "piedra"
    elif pc == 1:
        pc = "papel"
    elif pc == 2:
        pc = "tijera"
    print("PC: ", pc)

    if pc == "piedra" and jugador == "papel":
        print("Ganaste, Papel gana Piedra")
        score = 1

    elif pc == "papel" and jugador == "tijera":
        print("Ganaste, Tijera gana Papel")
        score = 1

    elif pc == "tijera" and jugador == "piedra":
        print("Ganaste, Piedra gana Tijera")
        score = 1

    if pc == "papel" and jugador == "piedra":
        print("Perdiste, Papel gana Piedra")
        score = 0

    elif pc == "tijera" and jugador == "papel":
        print("Perdiste, Tijera gana papel")
        score = 0

    elif pc == "piedra" and jugador == "tijera":
        print("Perdiste, Piedra gana tijera")
        score = 0

    elif pc == jugador:
        print("Empate")
        score = 0
    
    conexion=sqlite3.connect("arcade.db")
    conexion.execute("update gamer set score = score + ? where id = ?", (score,id))
    conexion.commit()
    conexion.close()

def segundoJuego(id,life):

    conexion=sqlite3.connect("arcade.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM palabras")
    
    rows = cursor.fetchall()
    lst = list()

    for row in rows:

        lst.append(row[1])

    conexion.close()
    
    palabra = random.choice(lst)
 
    lst = list()
    
    print('_' * len(palabra))
    
    while True:
    
        while True:
            option = input("Adivina una letra: ")
            if(len(option)!=1 and option.isnumeric()):
                print("Solo una letra")
            else:
                if option.lower() in lst:
                    print("Con esa letra ya lo habias intentado")
                else:
                    lst.append(option)
    
                    if option.lower() in palabra:
                        print("Felicidades adivinaste una letra")

                        conexion=sqlite3.connect("arcade.db")
                        conexion.execute("update gamer set score = score + ? where id = ?", (1,id))
                        conexion.commit()
                        conexion.close()

                        break
                    else:
                        life = life-1
                        print("Te haz equivocado y perdido una vida")
                        print("Te quedan " + str(life) + " vida")
                        break
    
        if life==0:
            print("Perdiste, la palabra secreta era: "+ palabra)
            break
    
        actual = ""
    
        letras = 0
        for letra in palabra:
    
    
            if letra in lst:
                actual = actual + letra
    
            else:
                actual = actual + "_"
                letras = letras + 1
    
        print(actual)
    
    
        if letras == 0:
            print("Ganaste")
            print("La palabra secreta es: " + palabra)
            break

def tercerJuego(): pass

if __name__ == "__main__":

    database()
    
    id = opcionTres()
    life = 3

    while True:

        print(end= "\n")
        print("ID jugador: " + id)
        print(end= "\n")

        print ("1. Selección del juego")
        print ("2. Registro del jugador")
        print ("3. Almacenamiento del puntaje del jugador")
        print ("4. Control de intentos máximos")
        print ("5. Ranking de Jugadores con mejor puntaje")
        print ("6. Salir")

        print(end= "\n")
        option = input('Ingrese Opcion: ')
        print(end= "\n")

        if option == "1": opcionUno(id,life)
        if option == "2": opcionDos()
        if option == "3": id = opcionTres()
        if option == "4": life = opcionCuatro()
        if option == "5": opcionCinco()
        if option == "6": break

