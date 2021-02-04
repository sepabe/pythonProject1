def main():
    arrnum1 = []
    arrnum2 = []
    count1 = 0
    count2 = 0
    MCD = 0
    pattern = ".0"

    # For itera dos veces por los dos numeros
    for x in range(2):
        num = int(input("Ingrese un numero entero: "))
        div = 1
        # For recorre las divisiones del numero desde el 1 hasta si mismo
        for y in range(num):
            # Validacion si la division da resto 0
            if str(num/div).endswith(pattern):
                # Validacion para guardar divisores del 1er o 2do numero
                if x==0:
                    arrnum1.append(div)
                    count1 += 1
                elif x==1:
                    arrnum2.append(div)
                    count2 += 1
            div += 1

    # Fors anidados para recorrer los arrays de divisores de los dos numeros
    for x in range(count1):
        for y in range(count2):
            # Validacion si es comun divisor Y tambien es mayor al ultimo valor comun (o 0 si es el primero)
            if arrnum1[x]==arrnum2[y] and arrnum1[x]>MCD:
                MCD = arrnum1[x]
    print("El maximo comun divisor entre esos numeros es:", MCD)
            
    
if __name__ == "__main__":
    main()