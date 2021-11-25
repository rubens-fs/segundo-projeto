nome = input('Qual é o seu nome? ')
print('É um prazer em te conhecer, {}!'.format(nome))
print('Quais foram seus valores de vendas nos meses de Janeiro, Fevereiro, Março e Abril, respectivamente?')
n1 = float(input('Mês de Janeiro: '))
n2 = float(input('Mês de Fevereiro: '))
n3 = float(input('Mês de Março: '))
n4 = float(input('Mês de Abril: '))
s = (n1 + n2 + n3 + n4) / 4
print('{0}, a média das suas vendas nos 4 meses: {1}, {2}, {3} e {4} é {5}!'.format(nome, n1, n2, n3, n4, s))

# Aqui exibiremos o resultado da média.
# Se o mesmo conseguiu um valor igual ou acima a 5000, ele ganhará um abono de 10%, senão, conseguirá um abono de 3%.

if s >= 5000:
    print('Parabéns, você vai receber um abono de 10%!')
else:
    print('Você vai receber um abono de 3%!')
