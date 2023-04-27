import unittest
from tentativa.Calculadora import Calculadora

class TesteDivisao(unittest.TestCase):

    def test_divisao_normal(self):
        self.assertEqual(Calculadora.divisao(10, 2), 5)
        self.assertEqual(Calculadora.divisao(6, 2), 3)
        self.assertEqual(Calculadora.divisao(10, 0), 'Erro: divisão por zero')
