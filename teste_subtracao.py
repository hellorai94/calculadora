import unittest
from tentativa.Calculadora import Calculadora

class TesteCalculadora(unittest.TestCase):
    def teste_subtracao(self):
        self.assertEqual(Calculadora.subtracao(5, 2), 3)
        self.assertEqual(Calculadora.subtracao(2, 5), -3)
        self.assertEqual(Calculadora.subtracao(13, 15), -2)