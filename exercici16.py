def main():
    mult = []
    num = int(input("Ingrese un numero entero entre 1 y 20 (inclusive): "))
    # Validacion del numero
    while num<1 or num>20:
        num = int(input("(!) Error. Ingrese un valor ENTERO del rango 1-20: "))
    x = 0
    # While que itera mientras que el resultado de los multiplos sea menor a 100
    while (num*x)<100:
        mult.append(num*x)
        x += 1
    print(f"Los multiplos de {num} son:", mult)

if __name__ == "__main__":
    main()
