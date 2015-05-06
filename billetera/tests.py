'''
Created on 6/5/2015

@author: Gabriel Iglesias  11-10476
         Susana Rodriguez  11-10893
         Mathieu De Valery 10-10193
'''
import unittest
from billetera import *

class TestBilletera(unittest.TestCase):


    def testInit(self):
        BilleteraElectronica(11223, "Pepe", "Juarez", 25893464, 12345)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()