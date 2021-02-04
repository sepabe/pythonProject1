def main():
    reg = int(input("¿Cuantos registros desea introducir? -> "))
    classrooms = {'classNum': list(),
                  'className': list(),
                  'IP': list(),
                  'PCs': list()}


    for x in range(reg):
        print("\nRegistro", x+1,
              "\nDatos del aula...")

        num = 0
        while num<1 or num>50:
            num = int(input(" Numero (1-50): "))

        name = input(" Nombre (6-9 caracteres): ")

        ip = "192.168."+input(" IP: 192.168.")

        pcs = 0.0
        while pcs<1 or pcs>20:
            pcs = int(input(" Numero de PCs (1-20): "))

        classrooms['classNum'].append(num)
        classrooms['className'].append(name)
        classrooms['IP'].append(ip)
        classrooms['PCs'].append(pcs)

    print("\n\t\t| Num.\t| Nombre\t| IP\t\t\t| Num. PCs\t|")
    for x in range(reg):
        print('Reg.{}\t| {} \t| {}\t| {}\t| {} \t\t|'.format(x+1, classrooms['classNum'][x], classrooms['className'][x], classrooms['IP'][x], classrooms['PCs'][x]))


""" PRINTAR DICCIONARIO HORIZONTAL
    for key in classrooms:
        print('')
        for x in range(reg):
            print('{}\t'.format(classrooms[key][x]), end='')
"""

""" PRINTAR DICCIONARIO CON LISTAS
    printList = classrooms['classNum']
    x=0
    print(printList[x])
"""

if __name__ == "__main__":
    main()