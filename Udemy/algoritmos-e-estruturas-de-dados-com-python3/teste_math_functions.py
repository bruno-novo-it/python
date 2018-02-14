import math_functions
import unittest

import os
import sys
import platform

# Classe para Testes e Verificar se um resultado 
class TestMathMethods(unittest.TestCase):

    def test_pot(self):
        self.assertEqual(1024, math_functions.pot(2,10))
    
    def test_fat(self):
        self.assertEqual(120,math_functions.fat(5))

#unittest.main()



#print(platform.system())