## Tarjetería Española
def cant(papel, plumon):

    plumon= plumon*35
    papel= papel*12
    if plumon>papel:
        total= papel
    elif papel>plumon:
        total= plumon
    return total

def  main():
  #escribe tu código abajo de esta línea
  papel= int(input('Dame la cantidad de pliegos de papel albanene: '))
  plumon= int(input('Dame la cantidad de plumones: '))

  print('El número máximo de tarjetas que se pueden hacer es: '+ str(cant(papel,plumon)))

if __name__ == '__main__':
    main()
