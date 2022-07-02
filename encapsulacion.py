import random


class CuentaBancaria():
    # Propiedades
    __numero_cuenta = ''
    titular = ''
    __saldo = 0

    # Constructor
    def __init__(self, titular):
        self.__generar_numero_cuenta()
        self.titular = titular

    #Get / Set

    # Permiso de lectura para leer la variable numero_cuenta que hemos hecho privada con la encapsulacion
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    # Metodos
    def __generar_numero_cuenta(self):
        self.__numero_cuenta = random.randint(0, 999999999999)

    def añadir_saldo(self, dinero):
        if dinero > 0 and dinero < 500:
            self.__saldo += dinero

    def sacar_dinero(self, dinero):
        if dinero > 0:
            self.__saldo -= dinero


mi_cuenta = CuentaBancaria('Luis Isarria')
print(mi_cuenta.get_numero_cuenta())
print(mi_cuenta.get_saldo())
mi_cuenta.añadir_saldo(500)
print(mi_cuenta.get_saldo())
mi_cuenta.sacar_dinero(99)
print(mi_cuenta.get_saldo())

