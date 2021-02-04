def main():
    nums = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ammount = 1
    position = 5
    count = 0
    
    # For para iterar 13 veces (13 lineas a printar)
    for x in range(13):
        index = 0
        # Se recorre el array de nums para printarlo
        for y in nums:
            # Si hay un 0 se printa un espacio, si hay un numero se printa el numero
            if nums[index] <= 0:
                print(' ', end = '')
            else:
                print(nums[index], end = '')
            index += 1
        
        print('')
        count += 1
        
        # Cuando se acaba de printar la linea mas larga y el array esta completo se ejecuta este if para arreglar la posicion
        if count == 7:
            position = 0
        aux = position
        
        if count < 7:
            ammount += 2
            for y in range(ammount):
                nums[aux] += 1
                aux += 1
            position -= 1
        elif count > 6:
            for y in range(ammount):
                nums[aux] -= 1
                aux += 1
            ammount -= 2
            position += 1
            
    
if __name__ == "__main__":
    main()