'''
Created on 6/5/2015

@author: susyroma
'''

from datetime import date

class Consumos():
    ''' Tipo de datos para gestionar la información de los consumos. '''


    def __init__(self, monto, anio, mes, dia, id_establecimiento):
        ''' (Consumo, float, int, int, int, int) -> NoneType
        
        Constructor de la clase.
        
        '''
        
        self.monto = monto
        self.fecha = date(anio, mes, dia)
        self.id_establecimiento = id_establecimiento
