def primerMenu():

    while True:

        try:
            numeroVacas = int(input('Ingrese numero de vacas: '))
            if numeroVacas >= 3 and numeroVacas <= 50:
                break
            else:        
                print("El numero tiene que estar entre 3 y 50", end= "\n")
                print(end= "\n")
        except ValueError:
            print("Error Solo Numeros", end= "\n")
            print(end= "\n")

    return numeroVacas


def segundoMenu(numeroVacas):

    while True:

        lst=list()
        mtr=list()

        for i in range(7):
            for j in range(numeroVacas):

                while True:

                    try:
                        litroLeche = float(input('Litros de leche, dia '+str(i+1)+',vaca '+str(j+1)+": "))
                        if litroLeche >= 0.0 and litroLeche <= 11.9:
                            break
                        else:        
                            print("El numero tiene que estar entre 0.0 y 11.9", end= "\n")
                            print(end= "\n")
                    except ValueError:
                        print("Error Solo Numeros", end= "\n")
                        print(end= "\n")

                lst.append(litroLeche)

            mtr.append(lst)
            lst=list()

        break
    
    return mtr


def tercerMenu(data):

    while True:

        print(end= "\n")

        print ("1. La producción total de leche del hato en cada uno de los sietes días.")
        print ("2. El día de la semana con mayor y menor producción.")
        print ("3. El número de la vaca que dio más leche en cada día.")
        print ("4. Visualizar Datos")
        print ("5. Regresar al Menu Principal")

        print(end= "\n")
        option = input('Ingrese Opcion: ')
        print(end= "\n")

        if option == "1": opcionUno(sumarProduccion(data))
        if option == "2": opcionDos(sumarProduccion(data))
        if option == "3": opcionTres(data)
        if option == "4": opcionCuatro(data)
        if option == "5": break


def sumarProduccion(mtr):

    fil,col = len(mtr),len(mtr[0])
    lst=list()

    for i in range(fil):
        lst.append(sum(mtr[i]))

    return lst


def opcionUno(lst):

    for i in range(len(lst)):
        print("Dia "+ str(i+1) +": "+ str(lst[i]))
    print(end= "\n")
    input('Presione cuaquier tecla para continuar')
    print(end= "\n")
    print(end= "\n")


def opcionDos(lst):

    print("Mayor Produccion: Dia " + str(lst.index(max(lst)) + 1))
    print("Menor Produccion: Dia " + str(lst.index(min(lst)) + 1))
    print(end= "\n")
    input('Presione cuaquier tecla para continuar')
    print(end= "\n")
    print(end= "\n")


def opcionTres(mtr):
    
    fil,col = len(mtr),len(mtr[0])
    for i in range(fil):

        print("Dia "+str(i+1)+": ",end= " ")

        for j in range(col): 
            if max(mtr[i]) == mtr[i][j]: 
                print("Vaca "+str(j+1),end= " ")

        print(end= "\n")
    print(end= "\n")
    input('Presione cuaquier tecla para continuar')
    print(end= "\n")
    print(end= "\n")
                

def opcionCuatro(mtr):

    fil,col = len(mtr),len(mtr[0])

    for i in range(fil):
        print("Dia "+str(i+1)+": ",end= " ")
        for j in range(col): 
            print(mtr[i][j],end= " ")
        print(end= "\n")

    print(end= "\n")
    input('Presione cuaquier tecla para continuar')
    print(end= "\n")
    print(end= "\n")

if __name__ == "__main__":

    while True:

        print(end= "\n")

        print ("1. Datos Nuevos")
        print ("2. Datos de Prueba")
        print ("3. Salir")

        print(end= "\n")
        option = input('Ingrese Opcion: ')
        print(end= "\n")

        if option == "1": 

            numeroVacas = primerMenu()
            litrosLeche = segundoMenu(numeroVacas)
            tercerMenu(litrosLeche)
            

        if option == "2": 
            
            litrosLeche=[[3,4,2,3,4],[2,3,4,5,5],[3,2,2,1,2],[1,1,1,1,1],[2,3,5,2,2],[4,3,4,5,1],[2,2,2,2,2]]
            tercerMenu(litrosLeche)

        if option == "3": break