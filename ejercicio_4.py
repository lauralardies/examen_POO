import random
from datetime import datetime

class Cuenta:

    def __init__(self) -> None:
        self.id = id
        self.nombre_titular = nombre_titular
        self.fecha_apertura = apertura
        self.num_cuenta = num_cuenta
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

class CuentaPlazoFijo:

    def __init__(self) -> None:
        self.id = id
        self.nombre_titular = nombre_titular
        self.fecha_apertura = apertura
        self.num_cuenta = num_cuenta
        self.saldo = 10000
        self.fecha_vencimiento = vencimiento
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

class CuentaVip:
    def __init__(self) -> None:
        self.id = id
        self.nombre_titular = nombre_titular
        self.fecha_apertura = apertura
        self.num_cuenta = num_cuenta
        self.saldo = 10000
        self.saldo_negativo = saldo_negativo

    def retirar_dinero(self):
        dinero_retirar = 78
        if dinero_retirar > (self.saldo_negativo + self.saldo):
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
        if dinero_transferir > (self.saldo_negativo + self.saldo):
            print("No puedes transferir esta cantidad dinero a otra cuenta.")
            exit
        else:
            self.saldo = self.saldo - dinero_transferir
            print("Se han transferido " + str(dinero_transferir) + "€.")

# CÓDIGO PRINCIPAL:

while True: # En este bucle se decide la cuenta bancaria que quiere el usuario:
    banco = int(input("Qué cuenta bancaria quieres crear?: \n - Para cuenta normal introduzca 1. \n - Para cuenta de plazo fijo introduzca 2. \n - Para cuenta VIP introduzca 3. \n"))

    if banco == 1 or banco == 2 or banco == 3: # Sabemos que ha seleccionado una opción correcta

        # El usuario nos indica su nombre
        nombre_titular = input("Por favor introduzca su nombre: ")
                
        # Decidimos la fecha de apertura y la de vencimiento
        inicio = datetime(2022, 3, 24)
        fin = datetime(3500, 1, 1)
        fecha_1 = inicio + (fin - inicio) * random.random()
        fecha_2 = inicio + (fin - inicio) * random.random()

        if fecha_1 > fecha_2 == True:
            vencimiento = fecha_1
            apertura = fecha_2
        else:
            vencimiento = fecha_2
            apertura = fecha_1

        # Seleccionamos el ID del usuario
        id = []
        for i in range(6): # Vamos a establecer que el ID va a ser sólo 6 números
            x = str(random.randrange(0,9,1))
            id.append(x)
        id = "".join(id)
 
        # Generamos el número de cuenta  
        num_cuenta = []
        for i in range(12):
            x = str(random.randint(0,9))
            num_cuenta.append(x)
        num_cuenta = "".join(num_cuenta)

        if banco == 1:
            cuenta = Cuenta()
            print("Usted ha escogido la cuenta normal.")
            break

        if banco == 2:
            cuenta = CuentaPlazoFijo()
            print("Usted ha escogido la cuenta de plazo fijo.")
            break

        if banco == 3:
            # Seleccionamos el saldo negativo:
            saldo_negativo = int(input("¿Cuánto saldo negativo quiere en su cuenta?: "))

            cuenta = CuentaVip()
            print("Usted ha escogido la cuenta VIP.")
            break
        
    else:
        print("Parece que no ha introducido un valor correcto, inténtelo de nuevo.")

# Creamos otro bucle para que el usuario pueda realizar acciones en su cuenta:
while True:
    accion = int(input("Decide las acciones que quieres realizar en tu cuenta: \n - Para retirar dinero pulse 1. \n - Para ingresar dinero pulse 2. \n - Para transferir dinero pulse 3. \n - Para salir del menú pulse 4. \n"))
    if accion == 1 or accion == 2 or accion == 3 or accion == 4: # Sabemos que ha seleccionado una opción correcta
        if accion == 1:
            cuenta.retirar_dinero()

        if accion == 2:
            cuenta.ingresar_dinero()

        if accion == 3:
            cuenta.transferir_dinero()
            
        if cuenta == 4:
            print("Ha seleccionado salir del menú.")
            exit()

        decision = input("¿Quiere hacer otra acción? [Y]/N: ")
        decision = decision.capitalize()
        if decision == "N":
            exit()
    else:
        print("Parece que no ha seleccionado una opción válida, escoja de nuevo.")