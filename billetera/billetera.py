'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476
         Susana Rodriguez  11-10893
         Mathieu De Valery 10-10193
'''
from recarga import *
 
class BilleteraElectronica():
    ''' Billetera electronica para realizar consumos via internet. '''


    def __init__(self, identificador, nombre, apellido, ci, pin):
        ''' (billeteraElectronica, int, str, str, int, int) -> NoneType
        
        Crea una billeteraElectronica para el usuario indicado. Inicialmente,
        se crea con un saldo de Bs. 0
                        
        '''
        
        self.identificador = identificador
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.pin = pin 
        self.saldo = 0.0
        self.fecha_ultMovimiento = None
        
    def consultarSaldo(self):
        ''' (BilleteraElectronica) -> int
        
        Devuelve el saldo con el que cuenta la billetera.
        
        '''
        
        return self.saldo
    
    def recargar(self, recarga):
        ''' (BilleteraElectronica, Recarga) -> int 
        
        Aumenta el saldo por el monto de la recarga.
        
        '''
        
        self.saldo += recarga.monto
        self.fecha_ultMovimiento = recarga.fecha
        return self.saldo