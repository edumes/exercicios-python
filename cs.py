print('calculadora simples de +')
n1 = float(input('digite aqui: '))
n2 = float(input('digite aqui: '))
conta = n1 + n2
print('resultado da conta: {}'.format(conta))
question = str(input('vc deseja adicionar mais algum numero?:'))
if question == 'sim':
    question1 = float(input('digite outro numero aqui: '))
    conta2 = conta + question1
    print('resultado da conta: {}'.format(conta2))
else:
    print('ok, seu resultado continua sendo {}'.format(conta))

