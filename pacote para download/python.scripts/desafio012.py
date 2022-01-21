preco=float(input('Qual o valor do produto?'))
novo=preco-(preco*5/100)
print('O valor do produto é R${:.2f}, com o desconto de 5% ele fica por {:.2f}.'.format(preco,novo))
