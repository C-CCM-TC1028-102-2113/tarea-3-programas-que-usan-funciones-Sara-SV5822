## Área de un rectángulo
def area(b, h):
    total=b*h
    return total

def main():
    b=float(input('Dame la base: '))
    h=float(input('Dame la altura: '))

    print('El área del rectángulo es: '+str(area(b,h)))


if __name__=='__main__':
    main()
