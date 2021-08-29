## Año bisiesto
def condition(year):
    if year%4==0 and year%100==0 and year%400!=0:
        resultado='False'
    elif year%4!=0:
        resultado='False'
    elif year%4==0 and year%400==0:
        resultado='True'
    elif year%4==0 and year%100!=0 and year%400!=0:
        resultado='True'
    return resultado

def main():
  #escribe tu código abajo de esta línea
  year=int(input(''))
  print(condition(year))

if __name__ == '__main__':
    main()
