from datetime import datetime

class Cuenta:

    def __init__(self) -> None:
        self.id =
        self.nombre_titular =
        self.fecha_apertura = 
        self.num_cuenta = 
        self.saldo = 10000
    
    def retirar_dinero(self):
        dinero_retirar = 78
        if dinero_retirar > self.saldo:
            print("No puedes retirar esta cantidad dinero de la cuenta.")
            exit
        else: 
            self.saldo = self.saldo - dinero_retirar
            print("Se han retirado " + str(dinero_retirar) + "€ a tu cuenta bancaria.")

    def ingresar_dinero(self):
        dinero_ingresar = 575
        self.saldo = dinero_ingresar + self.saldo
        print("Se han añadido " + str(dinero_ingresar) + "€ a tu cuenta bancaria.")

    def transferir_dinero(self):
        dinero_transferir = 2000
        if dinero_transferir > self.saldo:
            print("No puedes transferir esta cantidad dinero a otra cuenta.")
            exit
        else:
            self.saldo = self.saldo - dinero_transferir
            print("Se han transferido " + str(dinero_transferir) + "€.")

class CuentaPlazoFijo(Cuenta):

    def __init__(self) -> None:
        super().__init__()
        self.fecha_vencimiento = 
        self.fecha_actual = datetime.today()

    def retirar_dinero(self):
        dinero_retirar = 78
        if self.fecha_actual > self.fecha_vencimiento:
            dinero_retirar = dinero_retirar + (dinero_retirar * 0.05)
            if dinero_retirar > self.saldo:
                print("No puedes retirar esta cantidad dinero de la cuenta.")
                exit
            else: 
                self.saldo = self.saldo - dinero_retirar
                print("Se han retirado " + str(dinero_retirar) + "€ a tu cuenta bancaria.")

    def ingresar_dinero(self):
        dinero_ingresar = 575
        self.saldo = dinero_ingresar + self.saldo
        print("Se han añadido " + str(dinero_ingresar) + "€ a tu cuenta bancaria.")

    def transferir_dinero(self):
        dinero_transferir = 2000
        if dinero_transferir > self.saldo:
            print("No puedes transferir esta cantidad dinero a otra cuenta.")
            exit
        else:
            self.saldo = self.saldo - dinero_transferir
            print("Se han transferido " + str(dinero_transferir) + "€.")

class CuentaVip(Cuenta):
    def __init__(self) -> None:
        super().__init__()
        self.saldo_negativo =

    def retirar_dinero(self):
        dinero_retirar = 78
        if dinero_retirar > self.saldo_negativo:
            print("No puedes retirar esta cantidad dinero de la cuenta.")
            exit
        else: 
            self.saldo = self.saldo - dinero_retirar
            print("Se han retirado " + str(dinero_retirar) + "€ a tu cuenta bancaria.")

    def ingresar_dinero(self):
        dinero_ingresar = 575
        self.saldo = dinero_ingresar + self.saldo
        print("Se han añadido " + str(dinero_ingresar) + "€ a tu cuenta bancaria.")

    def transferir_dinero(self):
        dinero_transferir = 2000
        if dinero_transferir > self.saldo:
            print("No puedes transferir esta cantidad dinero a otra cuenta.")
            exit
        else:
            self.saldo = self.saldo - dinero_transferir
            print("Se han transferido " + str(dinero_transferir) + "€.")

# CÓDIGO PRINCIPAL:
