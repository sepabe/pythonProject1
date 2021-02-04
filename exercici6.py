from array import *
def main():
    value = int(input("Ingrese un valor entre 0 y 10 (inclusive): "))
    # Estructura repetitiva que itera hasta que se ingresa un numero del rango (0-10)
    while value<0 or value>10:
        value = int(input("EL VALOR DEBE SER UN NUMERO NATURAL, MINIMO 0 Y MAXIMO 10. INTENTE OTRA VEZ: "))
    print("¡Bien Hecho!")
    
if __name__ == "__main__":
    main()