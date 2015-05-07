'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476
         Susana Rodriguez  11-10893
         Mathieu De Valery 10-10193
'''

from datetime import date

class Recarga():
    ''' Tipo de datos para gestionar la información de las recargas. '''


    def __init__(self, monto, anio, mes, dia, id_establecimiento):
        ''' (Recarga, float, int, int, int, str) -> NoneType
        
        Constructor de la clase.
        
        '''
        
        self.monto = monto
        self.fecha = date(anio, mes, dia)
        self.id_establecimiento = id_establecimiento