velocidade = float(input('digite a velocidade do carro: '))
if velocidade <=90:
      print('ok vc esta dentro do limite.')
if velocidade >=90:
      print('vc ultrapassou o limite da velocidade')
      multa  = (velocidade-90) * 7
      print('sua MULTA foi de R${:.2f}'.format(multa))
print('tenha um bom dia, dirija com segurança!')
