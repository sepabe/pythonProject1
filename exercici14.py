def main():
    list = []
    sum = 0
    value = int(input(" ¿Cuantos valores desea ingresar? ->"))
    print(" Ingreselos, por favor:")
    for x in range(value):
        list.append(int(input("-> ")))
        sum += list[x]
    print(" Suma de los valores:", sum)
    
if __name__ == "__main__":
    main()