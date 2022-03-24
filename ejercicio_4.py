class Banco:

    def __init__(self) -> None:
        self.id =
        self.nombre_titular =
        self.fecha_apertura = 
        self.num_cuenta = 
        self.saldo = 
    
    def retirar_dinero(self):
        dinero_retirar = 
        if dinero_retirar > self.saldo:
            print("No puedes retirar esta cantidad dinero de la cuenta.")
            exit
        else: 
            self.saldo = self.saldo - dinero_retirar
            print("Se han retirado " + str(dinero_retirar) + "€ a tu cuenta bancaria.")

    def ingresar_dinero(self):
        dinero_ingresar =
        self.saldo = dinero_ingresar + self.saldo
        print("Se han añadido " + str(dinero_ingresar) + "€ a tu cuenta bancaria.")

    def transferir_dinero(self):
        dinero_transferir = 
        cuenta_transferir =
        if dinero_transferir > self.saldo:
            print("No puedes transferir esta cantidad dinero a otra cuenta.")
            exit
        else:
            self.saldo = self.saldo - dinero_transferir
            print("Se han transferido " + str(dinero_transferir) + "€ a la cuenta " + str(cuenta_transferir))

