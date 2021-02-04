import datetime
def main():
    seconds = int(input("Ingrese una cantidad de segundos"))
    print("Los segundos son [(n dias), hh:mm:ss] ->", str(datetime.timedelta(seconds=seconds)))
    
if __name__ == "__main__":
    main()