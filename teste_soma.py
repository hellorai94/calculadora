import unittest
from tentativa.Calculadora import Calculadora

class TesteCalculadora(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(Calculadora.soma(2, 3), 5)
        self.assertEqual(Calculadora.soma(-1, 1), 0)
        self.assertEqual(Calculadora.soma(28, 21), 49)
