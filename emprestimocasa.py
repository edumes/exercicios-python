casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: '))
anos = int(input('anos de financiamento: '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestaçao sera de {}'.format(prestaçao))
if prestaçao <= minimo:
      print('emprestimo cencedido!')
else:
      print('emprestimo negado')
