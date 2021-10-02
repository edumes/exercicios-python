from random import randint
from time import sleep
computador = randint(0, 5)
print('---' * 15)
print('vou pensar em um numero entre 0 a 5')
print('---' *15)
jogador = int(input('em que numero pensei: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
      print('parabens vc ganhou')
else:
      print('hahaha vc perdeu')
      print('eu pensei no numero {} e não no numero {}'.format(computador, jogador))
      print('otarrio')
