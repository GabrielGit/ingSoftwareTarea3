'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476.
         Susana Rodriguez  11-10893.
         Mathieu De Valery 10-10193.
'''

import sys
import unittest
from billetera import *
from xmlrpc.client import MAXINT, MININT

class TestBilletera(unittest.TestCase):

    # Casos de pruebas realizado a traves de la tecnica de TDD
    
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
        recarga1 = Recarga(100.0, 2015, 5, 2, "Comedor de Mys")
        b1.recargar(recarga1)
        consumo = Consumos(34.9, 2015, 5, 4, "Comedor de Mys")
        respuesta = b1.saldo - consumo.monto
        self.assertEqual(b1.consumir(consumo, 23456), respuesta)
        
    # Prueba interior apellidos con Acentos
    def testApellidosAcentos(self):
        BilleteraElectronica(11980,'Ana','Pérez',20394234,1234)
        
    # Prueba interior apellidos con Ñ
    def testApellidosEnie(self):
        BilleteraElectronica(22341,'Santiago','Patiño',20654745,2341)
        
    # Prueba interior apellidos con dieresis
    def testApellidosDieresis(self):
        BilleteraElectronica(37897,'Luisa','Ungüento', 2133461, 38917)
    
    # Prueba interior apellidos con guion
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
        
    # Prueba interior
    def testIDInvalida(self):
        self.assertRaises(Exception, BilleteraElectronica, 'as123','Juan','Carpio', 21234, 23456)
        
    # Prueba interior
    def testIDNegativo(self):
        self.assertRaises(Exception, BilleteraElectronica, -987,'Carlos','Rodriguez', 12234, 23456)

    # Prueba interior
    def testCedulaInvalida(self):
        self.assertRaises(Exception, BilleteraElectronica, 123,'Susana','Roma', '1234', 23456)
    
    # Prueba interior
    def testCedulaNegativa(self):
        self.assertRaises(Exception, BilleteraElectronica, 123,'Susana','Roma', -1234, 23456)

    # Prueba interior
    def testNombreInvalido(self):
        self.assertRaises(Exception, BilleteraElectronica, 123,'','Roma', 1234, 23456)
        
    # Prueba interior
    def testApellidoInvalid0(self):
        self.assertRaises(Exception, BilleteraElectronica, 123,'Susana','', 1234, 23456)
        
    # Prueba interior
    def testPinInvalido(self):
        self.assertRaises(Exception, BilleteraElectronica, 123,'Susana','Roma', 1234, '')
        
    # Prueba interior
    def testPinNegativo(self):
        self.assertRaises(Exception, BilleteraElectronica, 123,'Susana','Roma', 1234, -90)

    # Prueba interior
    def testRecargaNegativa(self):
        b1 = BilleteraElectronica(1579, 'Oscar', 'Guillen', 21444449, 1234)
        recarga3 = Recarga(-10, 2015, 5, 8, 'Taquilla Virtual')
        self.assertRaises(Exception, b1.recargar,recarga3)
        
    # Prueba interior
    def testConsumoNegativo(self):
        b1 = BilleteraElectronica(1579, 'Oscar', 'Guillen', 21444449, 1234)
        consumo3 = Consumos(-10, 2015, 5, 8, 'Taquilla Virtual')
        self.assertRaises(Exception, b1.consumir,consumo3,1234)

    # Prueba interior
    def testConsumoNoEntera(self):
        b1 = BilleteraElectronica(1579, 'Oscar', 'Guillen', 21444449, 1234)
        consumo3 = Consumos('a', 2015, 5, 8, 'Taquilla Virtual')
        self.assertRaises(Exception, b1.consumir,consumo3,1234)    
    
    # Prueba interior
    def testSaldoInsuficiente(self):
        b1 = BilleteraElectronica(1579, 'Fabio', 'Castro', 22324987, 2345)
        recarga4 = Recarga(20.0, 2015, 5, 8, 'Taquilla Virtual')
        b1.recargar(recarga4)
        consumo4 = Consumos(21,2015,5,9,'Subway')
        self.assertRaises(Exception, b1.consumir,consumo4,2345)
    
    # Prueba interior
    def testPinErroneo(self):
        b1 = BilleteraElectronica(1579, 'Carlos', 'Da Silva', 20642576, 7768)
        recarga5 = Recarga(30.0, 2015, 5, 8, 'Taquilla Virtual')
        b1.recargar(recarga5)
        consumo5 = Consumos(21,2015,5,9,'Subway')
        self.assertRaises(Exception, b1.consumir,consumo5,2345)  

    # Enriqueciendo la suite de pruebas

    #Prueba frontera
    def testMinimoConsumo(self):
        b1 = BilleteraElectronica(9876, 'Maria', 'Román', 20287352, 2760)
        recarga2 = Recarga(20.0, 2015, 2, 28, 'Taquilla Virtual')
        b1.recargar(recarga2)
        consumo = Consumos(0.0, 2015, 2, 21, 'Mathieu Spa')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo,2760)
        self.assertEqual(b1.saldo, resp)
        
    #Prueba frontera
    def testMaximoConsumoDecimal(self):
        b1 = BilleteraElectronica(9565, 'Ana', 'Anaco', 24287498, 28197)
        recarga = Recarga(MAXINT, 2015, 2, 6, 'Mater Salvatoris') 
        b1.recargar(recarga)
        consumo = Consumos(MAXINT, 2015, 2, 3, 'Acuario')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 28197)
        self.assertEqual(b1.saldo, resp)

    #Prueba frontera
    def testMaximoConsumoDecimal(self):
        b1 = BilleteraElectronica(9565, 'Ana', 'Anaco', 24287498, 28197)
        recarga = Recarga(sys.float_info.max, 2015, 2, 6, 'Mater Salvatoris') 
        b1.recargar(recarga)
        consumo = Consumos(sys.float_info.max, 2015, 2, 3, 'Acuario')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 28197)
        self.assertEqual(b1.saldo, resp)
        
    #Prueba frontera
    def testMinimoConsumoDecimal(self):
        b1 = BilleteraElectronica(9565, 'Ana', 'Anaco', 24287498, 28197)
        recarga = Recarga(sys.float_info.min, 2015, 2, 6, 'Mater Salvatoris') 
        b1.recargar(recarga)
        consumo = Consumos(sys.float_info.min, 2015, 2, 3, 'Acuario')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 28197)
        self.assertEqual(b1.saldo, resp)
         
    #Prueba frontera        
    def testRecargaMaxima(self):
        b1 = BilleteraElectronica(9876, 'Maria', 'Román', 20287352, 2760)
        recarga2 = Recarga(MAXINT, 2015, 2, 28, 'Taquilla Virtual')
        b1.recargar(recarga2)
        self.assertEqual(b1.saldo, MAXINT)
    
    #Prueba frontera    
    def testMinimaRecarga(self):
        b1 = BilleteraElectronica(9565, 'Jose', 'Duarte', 23456789, 2897)
        recarga = Recarga(0, 2015, 2, 6, 'La Salle')
        b1.recargar(recarga)
        resp = b1.saldo + recarga.monto
        self.assertEqual(b1.saldo, resp)
    
    #Prueba frontera   
    def testRecargaMaximaDecimal(self):
        b1 = BilleteraElectronica(9565, 'Jose', 'Duarte', 23456789, 2897)
        recarga = Recarga(sys.float_info.max, 2015, 2, 6, 'La Salle') 
        b1.recargar(recarga)
        self.assertEqual(b1.saldo, sys.float_info.max)
        
    #Prueba frontera
    def testRecargaMinimaDecimal(self):
        b1 = BilleteraElectronica(9565, 'Jose', 'Anaco', 24287498, 28197)
        recarga = Recarga(sys.float_info.min, 2015, 2, 6, 'Mater Salvatoris') 
        b1.recargar(recarga)
        self.assertEqual(b1.saldo, sys.float_info.min)
        
    #Prueba Esquina
    def testRecargaMaxDecimalConMinConsumoDecimal(self):
        b1 = BilleteraElectronica(9565, 'Jose', 'Duarte', 23456789, 2897)
        recarga = Recarga(sys.float_info.max, 2015, 2, 6, 'La Salle') 
        b1.recargar(recarga)
        consumo = Consumos(0.00000001, 2015, 3, 4, 'Litoral')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 2897)
        self.assertEqual(b1.saldo, resp)
        
    #Prueba Esquina
    def testRecargaMaxConMinConsumo(self):
        b1 = BilleteraElectronica(9565, 'Soyla', 'Mesa', 23456789, 2897)
        recarga = Recarga(MAXINT, 2015, 2, 6, 'Loyola') 
        b1.recargar(recarga)
        consumo = Consumos(0, 2015, 3, 4, 'Mercantil')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 2897)
        self.assertEqual(b1.saldo, resp)
        
    #Prueba Esquina
    def testRecargaMinDecimalConMaxConsumoDecimal(self):
        b1 = BilleteraElectronica(9565, 'Jose', 'Hermino', 23456789, 2897)
        recarga = Recarga(0.0000000001, 2015, 2, 6, 'USB') 
        b1.recargar(recarga)
        consumo = Consumos(0.00000000009, 2015, 3, 4, 'DACE')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 2897)
        self.assertEqual(b1.saldo, resp)
        
    #Prueba Esquina
    def testRecargaMinConMaxConsumo(self):
        b1 = BilleteraElectronica(9565, 'Deborah', 'Hartman', 23456789, 2897)
        recarga = Recarga(0, 2015, 2, 6, 'La Salle') 
        b1.recargar(recarga)
        consumo = Consumos(0, 2015, 3, 4, 'Litoral')
        resp = b1.saldo - consumo.monto
        b1.consumir(consumo, 2897)
        self.assertEqual(b1.saldo, resp)    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


