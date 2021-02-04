def main():
    start = int(input("Ingrese el primer numero del rango: "))
    finish = int(input("Ingrese el ultimo numero del rango: "))
    num = start
    div = 1
    count = 0
    pattern = ".0"

    # El for recorre el rango de numeros ingresado
    for x in range(start, finish):
        # El for itera la misma cantidad de veces que el valor del numero para dividir el mismo por todos los numeros desde el 1 hasta ese mismo numero
        for y in range(num):
            # Validacion. Si el resultado de dividir el numero de iteracion por el numero actual del rango es igual a cero o no
            if str(num/div).endswith(pattern):
                count += 1
            div += 1
        # Validacion. Si el resultado de la division fue cero solo dos veces significa que el numero es primo
        if count==2:
            print(num, "es primo !")
        num += 1
        # Reseteo de las variables para el siguiente numero del rango
        count = 0
        div = 1
    
if __name__ == "__main__":
    main()