from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
      print('VOCE TEM QUE SE ALISTAR!')
elif idade < 18:
      saldo = 18 - idade
      print('voce ainda não tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
      ano = atual + saldo
      print('seu alistamento sera em {}'.format(ano))
elif idade > 18:
      saldo = idade - 18
      print('voce ja deveria ter se alistado há {} anos'.format(saldo))
      ano = atual - saldo
      print('seu alistamento foi em {}'.format(ano))

