
def main():
    edad = int(input('Ingresa tu edad: '))
    if 0 < edad < 18:
        print('No cumples requisitos')
    elif edad <= 0:
        print('Respuesta incorrecta')
    else:
        idenficacion = input('¿Tienes identificación oficial? (s/n): ')
        if idenficacion == 's':
            print('Trámite de licencia concedido')
        elif idenficacion == 'n':
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')


if __name__ == '__main__':
    main()
