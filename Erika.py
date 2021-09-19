a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
operacao = input('Escolha uma operação matemática -Soma, subtração, multiplicação e divisão-:')
soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
if operacao == '+':
        print(soma)
elif operacao == '-':
        print(subtracao)
elif operacao == '/':
        print(divisao)
elif operacao == '*':
        print(multiplicacao)