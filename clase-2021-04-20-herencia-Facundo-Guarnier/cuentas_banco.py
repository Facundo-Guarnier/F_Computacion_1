class CuentaBancaria:
    def __init__(self):
        self.movimientos = []  


    def deposito(self, monto):
        self.movimientos.append(monto)
        

    def saldo_final(self):
        resultado = 0
        for movimiento in self.movimientos:
            resultado = resultado + movimiento
        return resultado


    def interes_mensual(self):
        if self.saldo_final() >= 0:
            interes = self.saldo_final() * 0.05
        else:
            interes = (self.saldo_final() * 0.20)

        self.deposito(interes)
        return interes


class CajaAhorro(CuentaBancaria):           #Puedo sacar plata hasta el disponible, el interes mensual: 5% del saldo de la cuenta.
    def extraccion(self, monto):
        if monto <= self.saldo_final():
            self.movimientos.append(-monto)
    

class CuentaCorriente(CuentaBancaria):      #tiene limite como credito, el interes es 5% si es positivo o 20% si es negativo.
    def __init__(self):
        super().__init__()
        self.limite_permitido = -3000  

    def extraccion(self, monto):
        if self.saldo_final() - monto >= self.limite_permitido:
            self.movimientos.append(-monto)



if __name__ == '__main__':
    caja_ahorro_gabriel = CajaAhorro()
    cuenta_corriente_casino = CuentaCorriente()

    caja_ahorro_gabriel.deposito(9999)
    print("Caja de ahorro <+9999>: " + str(caja_ahorro_gabriel.saldo_final()) + "\n")
    

    cuenta_corriente_casino.deposito(1000)
    print("Cuenta Corriente (casino) <+1000>: " + str(cuenta_corriente_casino.saldo_final()) + "\n")


    caja_ahorro_gabriel.extraccion(50)
    print("Caja de ahorro <-50>: " + str(caja_ahorro_gabriel.saldo_final()) + "\n")


    caja_ahorro_gabriel.extraccion(10000)                                       #La extracciones no se deberian poder.
    print("Caja de ahorro <-10000>: " + str(caja_ahorro_gabriel.saldo_final()) + "\n")


    cuenta_corriente_casino.extraccion(2000)
    print("Cuenta Corriente (casino) <-2000>: " + str(cuenta_corriente_casino.saldo_final()) + "\n")


    cuenta_corriente_casino.extraccion(2000)
    print("Cuenta Corriente (casino) <-2000>: " + str(cuenta_corriente_casino.saldo_final()) + "\n")


    cuenta_corriente_casino.extraccion(1000)                                    #La extracciones no se deberian poder.
    print("Cuenta Corriente (casino) <-1000>: " + str(cuenta_corriente_casino.saldo_final()) + "\n")
 


    print("Caja de ahorro <Movimientos>: " + str(caja_ahorro_gabriel.movimientos ))
    print("Cuenta Corriente (casino) <Movimientos>: " + str(cuenta_corriente_casino.movimientos) + "\n")

    
    caja_ahorro_gabriel.interes_mensual()                                       #Generar un mov positivo o negativo
    print("Caja de ahorro <Movimientos>: " + str(caja_ahorro_gabriel.movimientos ))
    print("Caja de ahorro <Con interes>: " + str(caja_ahorro_gabriel.saldo_final()) + "\n")

    
    cuenta_corriente_casino.interes_mensual()                                   #Generar un mov positivo o negativo
    print("Cuenta Corriente (casino) <Movimientos>: " + str(cuenta_corriente_casino.movimientos))
    print("Cuenta Corriente (casino) <Con interes>: " + str(cuenta_corriente_casino.saldo_final()) + "\n")
