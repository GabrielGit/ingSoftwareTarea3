'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476
         Susana Rodriguez  11-10893
         Mathieu De Valery 10-10193
'''
from recarga import *
from consumos import *
 
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
        
        if not isinstance(identificador,int):
            raise Exception ('El identificador solo admite numeros')
        
        elif (self.identificador < 0):
            raise Exception ('El identificador solo admite valores positivos')

        elif not isinstance(ci,int):
            raise Exception ('La cedula solo admite valores numericos')
        
        elif (self.ci < 0):
            raise Exception ('La cedula solo admite valores numericos positivos')
        
        elif (self.nombre == ''):
            raise Exception ('El nombre no puede ser un string vacio')
        
        elif (self.apellido == ''):
            raise Exception ('El apellido no puede ser un string vacio')
        
        elif not isinstance(pin,int):
            raise Exception ('El pin solo admite enteros')
        
        elif (self.pin < 0):
            raise Exception ('El pin solo admite valores numericos positivos')
        
    def consultarSaldo(self):
        ''' (BilleteraElectronica) -> int
        
        Devuelve el saldo con el que cuenta la billetera.
        
        '''
        
        return self.saldo
    
    def recargar(self, recarga):
        ''' (BilleteraElectronica, Recarga) -> int 
        
        Aumenta el saldo por el monto de la recarga.
        
        '''
        
        if (recarga.monto < 0.0):
            raise Exception("No está permitido hacer recargas de montos negativos.")
        
        elif not (isinstance(recarga.monto,float) or isinstance(recarga.monto,int)) :
           raise Exception ('La recarga solo admite valores numericos')
        
        
        self.saldo += recarga.monto
        self.fecha_ultMovimiento = recarga.fecha
        return self.saldo
    
    def consumir(self, consumo, pinUsuario):
        ''' (BilleteraElectronica, Consumo, int) -> int 
        
        Disminuye el saldo por el monto del consumo.
        
        '''

        if (self.pin != pinUsuario):
            raise Exception("El número PIN proporcionado no coincide.")
        
        elif (consumo.monto < 0.0):
            raise Exception("No está permitido hacer consumos de montos negativos.")
            
        elif (self.saldo < consumo.monto):
            raise Exception("Su saldo es insuficiente para realizar este consumo.")
        
        elif not (isinstance(consumo.monto,float)or isinstance(consumo.monto,int)) :
            raise Exception('El consumo solo admite valores numericos')
            
        else:
            self.saldo -= consumo.monto
            self.fecha_ultMovimiento = consumo.fecha
            
        return self.saldo

b1 = BilleteraElectronica(9876, 'Maria', 'Román', 20287352, 2760)