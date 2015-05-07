'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476
         Susana Rodriguez  11-10893
         Mathieu De Valery 10-10193.
'''
import unittest
from billetera import *

class TestBilletera(unittest.TestCase):

    #Prueba interior
    def testInit(self):
        BilleteraElectronica(11223, "Pepe", "Juarez", 25893464, 12345)
        
    #Prueba interior, de existencia    
    def testConsultarSaldoExiste(self):
        b1 = BilleteraElectronica(11223, "Pepe", "Juarez", 25893464, 12345)
        b1.consultarSaldo()
    
    #Prueba interior
    def testConsultarSaldo(self):
        b1 = BilleteraElectronica(1000, "Pepe", "Juarez", 24222691, 1532)
        self.assertEqual(b1.consultarSaldo(), 0.0)
    
    #Prueba interior, de existencia    
    def testCrearRecarga(self):   
        Recarga(22.4, 2015, 5, 5, "Comedor de Mys") 
    
    #Prueba interior    
    def testRevisarRecarga(self):
        b1 = BilleteraElectronica(11223, "Pedro", "Rondon", 25674667, 54321)
        recarga = Recarga(65.4, 2015, 6, 4, "Comedor de Estudiantes")
        resp = b1.saldo + recarga.monto
        self.assertEqual(b1.recargar(recarga), resp)
        
    #Prueba interior, de existencia  
    def testCrearConsumo(self):   
        Consumos(22.4, 2015, 5, 5, "Comedor de Estudiantes") 
    
    #Prueba interior
    def testRevisarConsumo(self):
        b1 = BilleteraElectronica(11103, "Ana", "De Valery", 21014266, 23456)
        recarga1 = Recarga(100, 2015, 5, 2, "Comedor de Mys")
        b1.recargar(recarga1)
        consumo = Consumos(34.9, 2015, 5, 4, "Comedor de Mys")
        respuesta = b1.saldo - consumo.monto
        self.assertEqual(b1.consumir(consumo, 23456), respuesta)
        
    # Apellidos con Acentos
    def testApellidosAcentos(self):
        BilleteraElectronica(11980,'Ana','Pérez',20394234,1234)
        
    # Apellidos con Ñ
    def testApellidosEnie(self):
        BilleteraElectronica(22341,'Santiago','Patiño',20654745,2341)
        
    # Apellidos con dieresis
    def testApellidosDieresis(self):
        BilleteraElectronica(37897,'Luisa','Ungüento', 2133461, 38917)
    
    # Apellidos con guion
    def testApellidosGuion(self):
        BilleteraElectronica(42435,'morris','Iglesias-Monedero',4678039, 34213)
        
    # Prueba interior. Se prueban las funcionalidades de recarga, consumo, y saldo.    
    def testSaldoCero(self):
        b1 = BilleteraElectronica(9876, "Marisela", "Del Valle", 20287352, 2760)
        recarga2 = Recarga(95.8, 2015, 2, 28, "Taquilla Virtual")
        b1.recargar(recarga2)
        consumo2 = Consumos(95.8, 2015, 3, 4, "Estacionamiento C.C. Metrocenter")
        b1.consumir(consumo2, 2760)
        self.assertEqual(b1.saldo, 0.0)       
        
                     


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()