while True:

    try:
        nv = int(input('Ingrese numero de vacas: '))
        if nv >= 3 and nv <= 50:
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
        for j in range(0,nv):

            while True:



                try:
                    nv = int(input('Ingrese numero de vacas: '))
                    if nv >= 3 and nv <= 50:
                        break
                    else:        
                        print("El numero tiene que estar entre 3 y 50", end= "\n")
                        print(end= "\n")
                except ValueError:
                    print("Error Solo Numeros", end= "\n")
                    print(end= "\n")

            lst.append(input("Dia: "+str(i+1)+", Vaca: "+str(j+1)+" "))

        mtr.append(lst)
        lst=list()
    break

 



while True:

    print ("1. Opcion 1")
    print ("2. Opcion 2")
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    option = input('Ingrese Opcion')

    if option == "4": break