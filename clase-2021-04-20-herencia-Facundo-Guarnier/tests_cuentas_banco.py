import unittest
from cuentas_banco import CajaAhorro, CuentaCorriente


class TestCajaAhorro(unittest.TestCase):

    def test_saldo_inicial(self):
        cuenta_ahorro = CajaAhorro()
        self.assertEqual(cuenta_ahorro.saldo_final(), 0)

    def test_deposito_inicial(self):
        cuenta_ahorro = CajaAhorro()
        cuenta_ahorro.deposito(100)
        self.assertEqual(cuenta_ahorro.saldo_final(), 100)

    def test_deposito_siguiente(self):
        cuenta_ahorro = CajaAhorro()
        cuenta_ahorro.deposito(200)
        cuenta_ahorro.deposito(300)
        self.assertEqual(cuenta_ahorro.saldo_final(), 500)

    def test_extraccion_con_saldo(self):
        cuenta_ahorro = CajaAhorro()
        cuenta_ahorro.deposito(200)
        cuenta_ahorro.extraccion(100)
        self.assertEqual(cuenta_ahorro.saldo_final(), 100)

    def test_extraccion_sin_saldo(self):
        cuenta_ahorro = CajaAhorro()
        cuenta_ahorro.extraccion(100)
        self.assertEqual(cuenta_ahorro.saldo_final(), 0)

    def test_interes_mensual(self):
        cuenta_ahorro = CajaAhorro()
        cuenta_ahorro.deposito(100)
        self.assertEqual(cuenta_ahorro.interes_mensual(), 5)
        self.assertEqual(cuenta_ahorro.saldo_final(), 105)


class TestCuentaCorriente(unittest.TestCase):

    def test_deposito(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(100)
        self.assertEqual(cuenta_corriente.saldo_final(), 100)

    def test_extraccion(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.extraccion(50)
        self.assertEqual(cuenta_corriente.saldo_final(), -50)

    def test_saldo(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(100)
        cuenta_corriente.extraccion(50)
        self.assertEqual(cuenta_corriente.saldo_final(), 50)

    def test_interes_mensual_saldo_positivo(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.deposito(100)
        self.assertEqual(cuenta_corriente.interes_mensual(), 5)
        self.assertEqual(cuenta_corriente.saldo_final(), 105)

    def test_interes_mensual_saldo_negativo(self):
        cuenta_corriente = CuentaCorriente()
        cuenta_corriente.extraccion(100)
        self.assertEqual(cuenta_corriente.interes_mensual(), -20)
        self.assertEqual(cuenta_corriente.saldo_final(), -120)


if __name__ == '__main__':
    unittest.main()