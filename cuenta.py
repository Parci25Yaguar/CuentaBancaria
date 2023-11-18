from random import randint

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre   = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numeroCuenta, saldo):
        super().__init__(nombre, apellido)
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Tu ID de tu cuenta es {self.numeroCuenta} y tu saldo es : {self.saldo}'
    
    def despositar(self):
        deposito = 'x'

        while not deposito.isnumeric():
            deposito = (input('Digite el monto a depostitar ($): '))
            if deposito.isnumeric():
                self.saldo += int(deposito)
                print('El depostivo se ha realizado correctamente :D')
                print(f'El nuevo saldo es de {self.saldo}')

    def retirar(self):
        retiro = 'x'
        while not retiro.isnumeric():
            if self.saldo == 0:
                print(f'{self.nombre} Su cuenta no tiene fondos')
                break

            if self.saldo > 0:
                print(f'Tiene disponible para retirar ${self.saldo}')
                retiro = input('Digite el monto a retirar: ')

                if int(retiro) > int(self.saldo):
                    print(f'El Monto a retirar en la cuenta {self.numeroCuenta} es Mayor a lo que tiene en la cuenta')
                else:
                    self.saldo -= int(retiro)
                    print(f'El retiro de los ${retiro} ha sido exitoso, le queda ${self.saldo}')

#Crear Usuario de la Cuenta
def crearUsuario():
    nombre       = input('Escriba su Nombre: ')
    apellido     = input('Escriba sus Apellidos: ')
    numeroCuenta = randint(20000, 30000)
    saldo        = randint(10000,20000)
    
    #Instancia de la Clase Cliente
    cliente = Cliente(nombre, apellido, numeroCuenta, saldo)
    return cliente

#Pantalla de Seleccion
def inicio():
    usuario  = crearUsuario()
    fin      = False
    opciones = 0

    while not fin:
        #Opciones de Inicio
        print('''
            Elija la opciones que quiera
            [1] - Depositar
            [2] - Retirar
            [3] - Ver Saldo
            [4] - Salir''')

        print('')

        opciones = int(input('Ingresa opcion: '))

        if opciones == 1:
            usuario.despositar()
        elif opciones == 2:
            usuario.retirar()
        elif opciones == 3:
            print(str(usuario))
        elif opciones == 4:
            fin = True
        
    
inicio()