def main():
    var1 = int(input(" Ingrese var1: "))
    var2 = int(input(" Ingrese var2: "))
    # Hago las asignaciones juntas asi los valores cambian sin perderse ninguno
    var1, var2 = var2, var1
    print("Valor de var1:", var1,
          "\nValor de var2:", var2)
    
if __name__ == "__main__":
    main()