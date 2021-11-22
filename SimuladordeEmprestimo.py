nome = input(' Olá, qual é seu nome?')
print('É um prazer {}!Eu sou a SimulaTudo :)'.format(nome))
valor = int(input('Para começarmos a simulação, qual valor você deseja para financiamento?'))
if valor > 0:
    print('Humm,ok! Vou precisar de mais alguns dados...')
elif valor < 0:
    print('ops! Valor indisponível :(')
salario = float(input('Nós nem nos conhecemos ainda rs, mas, quanto você recebe de salário? '))
parcelas = float(input('Certo, e em quantas vezes você deseja parcelar este empréstimo?'))
if parcelas > 24:
    print('Esta quantidade excede o nosso limite :(')
if parcelas < 24:
    print('Tudo bem!')
#simulacao
input('{} em {} vezes,correto?'.format(valor, parcelas))
print('Valor da Parcela:')
print( valor / parcelas)
if valor / parcelas > 0.30 * salario:
    print('Seu emprestimo foi negado :( !')
else:
    print('Parabéns! Seu empréstimo foi pré-aprovado!!')
    
    
    
