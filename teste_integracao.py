import unittest
from tentativa.Calculadora import Calculadora

class TesteIntegracao(unittest.TestCase):
    def test_minha_funcao(self):
        self.assertEqual(Calculadora.soma(2, 3), 5)
        self.assertEqual(Calculadora.subtracao(5, 2), 3)
        self.assertEqual(Calculadora.multiplicacao(2, 3), 6)
        self.assertEqual(Calculadora.divisao(10, 0), 'Erro: divisão por zero')

if __name__ == '__main__':
    unittest.main()
