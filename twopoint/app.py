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