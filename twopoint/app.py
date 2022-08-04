from operator import le


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

            for j in range(0,numeroVacas):

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


def tercerMenu():

    while True:

        print ("1. Produccion Total")
        print ("2. mayor menor")
        print ("3. numero de")
        print ("4. Salir")

        option = input('Ingrese Opcion')

        if option == "1": break

        if option == "2": break

        if option == "3": break

        if option == "4": break


def sumarProduccion(mtr):

    fil,col = len(mtr),len(mtr[0])

    print(fil)
    print(col)


if __name__ == "__main__":

    #numeroVacas = primerMenu()
    #litrosLeche = segundoMenu(numeroVacas)

    litrosLeche=[[3,4,2,3,4],[2,3,4,5,5],[3,2,2,1,2],[1,1,1,1,1],[2,3,5,2,2],[4,3,4,5,1],[2,2,2,2,2]]

    sumarProduccion(litrosLeche)


    
