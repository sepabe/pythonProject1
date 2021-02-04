def main():
    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    # La funcion dictionary no permite la repeticion de las claves que se le indican
    a = list(dict.fromkeys(a))
    print(a)
    
if __name__ == "__main__":
    main()
