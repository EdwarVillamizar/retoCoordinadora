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
        #print("se creo la tabla gamer")   
       
        conexion.commit()    

    except sqlite3.OperationalError:
        pass
        #print("La tabla gamer ya existe")   

    try:
        conexion.execute("""create table palabras(
                                id integer primary key autoincrement,
                                name text,
                            )""")

        palabras = ['hola','perro','gato']

        cursor = conexion.cursor()
        cursor.executemany('INSERT INTO palabra VALUES(?,?,?);',palabras);
    
       
        conexion.commit()    

    except sqlite3.OperationalError:
        pass
        #print("La tabla gamer ya existe")   

    conexion.execute("INSERT OR IGNORE INTO gamer(id,name,score) values (?,?,?)", (1,"Player 1",0))
    conexion.commit() 

    conexion.close()

def opcionUno(id):

    print(end= "\n")

    print ("1. Piedra Papel Tijera.")
    print ("2. Ahorcado.")
    print ("3. Astucia Naval.")

    print ("4. Regresar")

    print(end= "\n")
    option = input('Ingrese Opcion: ')
    print(end= "\n")

    if option == "1": primerJuego(id)
    if option == "2": segundoJuego(id)
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

def opcionCuatro(): pass

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
        print("Ganaste, Papel envulve Piedra")
        score = 1

    elif elijePc == "papel" and elijeUsuario == "tijera":
        print("Ganaste, Tijera corta Papel")
        score = 1

    elif elijePc == "tijera" and elijeUsuario == "piedra":
        print("Ganaste, Piedra pisa Tijera")
        score = 1

    if elijePc == "papel" and elijeUsuario == "piedra":
        print("Perdiste, Papel envulve Piedra")
        score = 0

    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("Perdiste, Tijera corta papel")
        score = 0

    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("Perdiste, Piedra pisa tijera")
        score = 0

    elif elijePc == elijeUsuario:
        print("Empate")
        score = 0
    
    conexion=sqlite3.connect("arcade.db")
    conexion.execute("update gamer set score = score + ? where id = ?", (score,id))
    conexion.commit()
    conexion.close()

def segundoJuego(id):
    
    palabra_secreta = "hola"
    vidas = 5
 
    lista_letras_adivinadas = []
    
    ## Imprimimos la palabra sin letras
    print('_' * len(palabra_secreta))
    
    while True:
    
        while True:
            letra_adivinada = input("Adivina una letra: ")
            if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
                print("Eso no es una letra intenta con una sola letra")
            else:
                if letra_adivinada.lower() in lista_letras_adivinadas:
                    print("Ya habias intentado con esa letra intenta con otra por favor")
                else:
                    lista_letras_adivinadas.append(letra_adivinada)
    
                    if letra_adivinada.lower() in palabra_secreta:
                        print("Felicidades adivinaste una letra")
                        break
                    else:
                        vidas = vidas-1
                        print("Te haz equivocado y perdido una vida")
                        print("Te quedan " + str(vidas) + " vidas")
                        break
    
        if vidas==0:
            print("Haz perdido la palabra secreta era: "+ palabra_secreta)
            break
    
    
        estatus_actual = ""
    
        letras_faltantes = 0
        for letra in palabra_secreta:
    
    
            if letra in lista_letras_adivinadas:
                estatus_actual = estatus_actual + letra
    
            else:
                estatus_actual = estatus_actual + "_"
                letras_faltantes = letras_faltantes + 1
    
        ## Imprimir palabra con algunas letras
        print(estatus_actual)
    
    
        if letras_faltantes == 0:
            print("Felicidades haz ganado")
            print("La palabra secreta es: " + palabra_secreta)
            break

if __name__ == "__main__":

    database()
    
    id = opcionTres()

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

        if option == "1": opcionUno(id)
        if option == "2": opcionDos()
        if option == "3": id = opcionTres()
        if option == "4": pass
        if option == "5": opcionCinco()
        if option == "6": break

