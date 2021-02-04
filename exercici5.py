from array import *
def main():
    
    tableOf = -1
    # Se itera 11 veces para las tablas del 0-10
    for x in range(11):
        print("")
        multiplied = 0
        table = [[]]
        tableOf += 1
        print("Tabla del", tableOf)
        i = 0
        # Se asignan los valores de la tabla y se printar para reutilizar la matriz
        for y in range(10):
            multiplied += 1
            # Se insertan los datos en el array
            table.insert(i, [tableOf, multiplied, tableOf*multiplied])
            # Se printa la linea actual del array
            print(table[y][0], "x", table[y][1], "=", table[y][2])
            i += 1
    
if __name__ == "__main__":
    main()