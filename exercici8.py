from array import *
def main():
    num = float(input("Ingrese un valor en centimetros: "))
    print("El valor en pulgadas es: ", round(num/2.54, 4))
    
if __name__ == "__main__":
    main()