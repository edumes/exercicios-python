print('--------------MEDIA-------------')
av1 = float(input('digite a primeira nota: '))
av2 = float(input('digite a segunda nota: '))
av3 = float(input('digite a terceira nota: '))
media = (av1 + av2 + av3)/3
if media <=5.7:
      print('sua nota esta abaixo da media!')
if media >=6:
      print('parabens sua nota esta AZUL')
if media ==5.9:
      print('sua nota sera arredondada para 6')
      print('sua media arredondada é 6.0')
print('sua media é de {}'.format(media))

