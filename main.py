from tentativa.Calculadora import Calculadora

def menu():
    print("======Selecione a opção desejada======")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("=======================================")

def operacaoes(opcao, num1, num2):
    calc = Calculadora()

    if opcao == '1':
        resultado = calc.soma(num1, num2)
    elif opcao == '2':
        resultado = calc.subtracao(num1, num2)
    elif opcao == '3':
        resultado = calc.multiplicacao(num1, num2)
    elif opcao == '4':
        resultado = calc.divisao(num1, num2)
    else:
        resultado = None
    return resultado

def main():
    while True:
        menu()
        opcao = input("Por favor, escolha a sua opção: ")
        try:
            num1 = float(input("Por favor, digite o primeiro número: "))
            num2 = float(input("Por favor, digite o segundo número: "))
            resultado= operacaoes(opcao, num1, num2)
            if resultado is not None:
                print('Resultado: ', resultado)
            else:
                print("Opção inválida")
        except ValueError:
            print("Por favor, digite um número válido.")
        continuar = input("Deseja realizar outra operação? (S/N) ")
        if continuar.upper() == 'N':
            break

if __name__ == '__main__':
    main()
