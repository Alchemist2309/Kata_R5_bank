import datetime

transacciones = []


def deposit():
    while True:
        consulta = input("¿Desea ingresar un depósito? (s/n): ")
        if consulta.lower() == 'n':
            break
        elif consulta.lower() == 's':
            monto = float(input("Ingrese monto a depositar: "))
            if monto <= 0:
                print("El monto ingresado no es correcto")
            else:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                transacciones.append((date, monto))
                print(f"Se ha depositado {monto} correctamente.")
    withdraw()



def withdraw():
    while True:
        consulta_retiro = input("¿Desea hacer un retiro? (s/n): ")
        if consulta_retiro.lower() == 'n':
            print_statement()
            break
        elif consulta_retiro.lower() == 's':
            retiro = float(input("Ingrese la cantidad del retiro"))
            if retiro <= 0:
                print("Digito un valor incorrecto o no tiene fondos suficiente:")
            else:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                transacciones.append((date, - retiro))
                print(f"Se ha retirado ${retiro} correctamente.")


def print_statement():
    saldo_actual = 0
    print(f"Fecha|| Monto|| Balance")
    for fecha, monto in transacciones:
        saldo_actual += monto
        print(f"{fecha}|| {monto}|| {saldo_actual}")


deposit()
