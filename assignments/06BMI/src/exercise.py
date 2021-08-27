def main():
    peso = float(input('Peso en kg: '))
    altura = float(input('Altura en m: '))
    if peso <=0 or altura <=0:
        print('Revisa tus datos, alguno de ellos es erróneo.')
    else:
        indice = peso/altura**2
        if indice < 20:
            print('PESO BAJO')
        elif 20 <= indice < 25:
            print('NORMAL')
        elif 25 <= indice < 30:
            print('SOBREPESO')
        elif 30 <= indice < 40:
            print('OBESIDAD')
        else:
            print('OBESIDAD MORBIDA')

if __name__=='__main__':
    main()