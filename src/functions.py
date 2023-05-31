def main_bank():
    while True:
        print('ingrese la opción segun su operación a realizar')
        option = int(input('\n 1. amount \n 2. withdraw \n 3. extracts \n'))
        if option == 0:
            exit()
        elif option == 1:
            amount()
        elif option == 2:
            withdraw()
        elif option == 3:
            extracts()
        else:
            print('invalid options')


def amount():
    print('monto a depositar')


def withdraw():
    print('monto a retirar')


def extracts():
    print('descarga tu extracto')

main_bank()
