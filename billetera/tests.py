'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476
         Susana Rodriguez  11-10893
         Mathieu De Valery 10-10193.
'''
import unittest
from billetera import *

class TestBilletera(unittest.TestCase):


    def testInit(self):
        BilleteraElectronica(11223, "Pepe", "Juarez", 25893464, 12345)
        
    def testConsultarSaldoExiste(self):
        b1 = BilleteraElectronica(11223, "Pepe", "Juarez", 25893464, 12345)
        b1.consultarSaldo()
        
    def testConsultarSaldo(self):
        b1 = BilleteraElectronica(1000, "Pepe", "Juarez", 24222691, 1532)
        self.assertEqual(b1.consultarSaldo(), 0.0)
        
    def testCrearRecarga(self):   
        Recarga(22.4, 2015, 5, 5, "Comedor de Mys") 
        
    def testRevisarRecarga(self):
        b1 = BilleteraElectronica(11223, "Pedro", "Rondon", 25674667, 54321)
        recarga = Recarga(65.4, 2015, 6, 4, "Comedor de Estudiantes")
        resp = b1.saldo + recarga.monto
        self.assertEqual(b1.recargar(recarga), resp)
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()