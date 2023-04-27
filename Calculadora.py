# criacao da classe Calculadora com os métodos estáticos das operações básicas

class Calculadora:

    @staticmethod
    def soma(num1, num2):
        return num1 + num2

    @staticmethod
    def subtracao(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicacao(num1, num2):
        return num1 * num2

    @staticmethod
    def divisao(num1, num2):
        if num2 == 0:
            return "Erro: divisão por zero"
        return num1 / num2