from array import *
def main():
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("Ingrese el segundo numero entero: "))
    num3 = int(input("Ingrese el tercer numero entero: "))
    # Valida si los tres numeros son iguales
    if num1==num2 and num1==num3:
        for x in range(3):
            print(num1+num2+num3, end = ' ')
    else:
        print(num1+num2+num3, end = ' ')
    
if __name__ == "__main__":
    main()