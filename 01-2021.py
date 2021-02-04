def main():
    reg = int(input("¿Cuantos registros desea introducir? -> "))
    classrooms = {'classNum': list(),
                  'className': list(),
                  'IP': list(),
                  'PCs': list()}


    for x in range(reg):
        print("Registro", x+1)

        num = 0
        while num<1 or num>50:
            num = int(input(" Ingrese el numero del aula: "))

        name = input(" Ingrese el nombre del aula: ")

        ip = input(" Ingrese la ip del aula: ")

        pcs = 0.0
        while pcs<1 or pcs>20:
            pcs = int(input(" Ingrese el numero de PCs: "))

        classrooms['classNum'].append(num)
        classrooms['className'].append(name)
        classrooms['IP'].append(ip)
        classrooms['PCs'].append(pcs)

    print("----------------------------")
    for x in classrooms:
        print(classrooms[x])
    print("----------------------------")
    for x in classrooms['classNum']:
        print(x)
        for y in classrooms['className']:
            print(y)
            for z in classrooms['IP']:
                print(z)
    print("----------------------------")
    for x in classrooms.values():
        print(x)




""" HOW TO PRINT VALUES FROM DICTIONARIES
    printList = classrooms['classNum']
    x=0
    print(printList[x])
"""

if __name__ == "__main__":
    main()