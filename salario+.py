salario = float(input('digite o salario atual: '))
if salario <= 1250:
      novo = salario + (salario * 15 / 100)
else:
      novo = salario + (salario * 10 / 100)
print('o salario que estava custando era de {:.2f} e o que passou a custar agora foi de {:.2f}'.format(salario, novo))
