def main():
    num = []
    sum = 0
    
    print("Ingrese 10 numeros decimales: ")
    # El for itera 10 veces para que el usuario ingrese 10 valores decimales
    for x in range(10):
        # Añade el input transformado a float en la lista num
        num.append(float(input("->")))
        # Suma los valores que se ingresan
        sum += num[x]

    print("Media:", sum/10)
    
if __name__ == "__main__":
    main()