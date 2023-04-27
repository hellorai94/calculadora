import unittest
from tentativa.Calculadora import Calculadora

class TesteCalculadora(unittest.TestCase):
    def teste_multiplicacao(self):
        self.assertEqual(Calculadora.multiplicacao(2, 3), 6)
        self.assertEqual(Calculadora.multiplicacao(12, 5), 60)
        self.assertEqual(Calculadora.multiplicacao(-2, 15), -30)
