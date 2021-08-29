## Volumen de un prisma rectangular
def area(b, h):
    area_rec=b*h
    return area_rec

def vol(prof, cara):
    volumen= cara*prof
    return volumen

def main():
  #escribe tu código abajo de esta línea
  b=float(input('Dame la base: '))
  h=float(input('Dame la altura: '))
  prof=float(input('Dame la profundidad: '))
  cara=area(b,h)
  print('El volumen del prisma es: '+ str(vol(prof, cara)))

if __name__ == '__main__':
    main()
