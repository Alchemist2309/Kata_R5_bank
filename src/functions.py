import datetime


def main_bank():
    while True:
        print('\n 1. Deposito \n 2. Retiro \n 3. Extracto \n 0. para Salir \n')
        option = input("Ingrese la operación que desea realizar: ")
        if option.isdigit():
            option = int(option)
            if option == 0:
                exit()
            elif option == 1:
                deposit()
            elif option == 2:
                withdraw()
            elif option == 3:
                print_statement()
            else:
                print('La opción que ha digitado es incorrecta, intentelo nuevamente ')
        else:
            print('solo puedes ingresar opciones en numeros')


transactions = []


def deposit():
    while True:
        consult = input("Dijite S para realizar un deposito o digite N Para salir: ")
        if not consult.isalpha():
            print("El valor ingresado no es correcto")
        elif consult.lower() == 'n':
            break
        elif consult.lower() == 's':
            monto = float(input("Ingrese monto a depositar: "))
            if monto <= 0:
                print("El monto ingresado no es correcto")
            else:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                transacciones.append((date, monto))
                print(f"Se ha depositado {monto} correctamente.")


def withdraw():
    while True:
        consulta_retiro = input("Dijite S para realizar un retiro o digite N Para salir:  ")
        if consulta_retiro.lower() == 'n':
            break
        elif consulta_retiro.lower() == 's':
            retiro = float(input("Ingrese la cantidad del retiro: "))
            if retiro <= 0:
                print("Digito un valor incorrecto o no tiene fondos suficiente")
            else:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                transactions.append((date, - retiro))
                print(f"Se ha retirado ${retiro} correctamente.")


def print_statement():
    saldo_actual = 0
    print(f"Fecha|| Monto|| Balance")
    for fecha, cash in transactions:
        saldo_actual += cash
        print(f"{fecha}|| {cash}|| {saldo_actual}")


main_bank()
