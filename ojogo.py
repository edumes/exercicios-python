import sys
import pygame
pygame.init()
print("O JOGO")
print("------")
print("use o numero 1 para sim e o numero 2 para não.")
print("----------------------------------------------")
question1 = int(input('deseja continuar?:'))
if question1 <= 1:
         print('carregando...')
if question1 >= 2:
      print('ok. Tchau :(')
      print('feche o jogo se nao quiser continuar!')
print('-----------------------------------------------')
question2 = int(input('primeiro inimigo! Deseja ataca-lo?:'))
if question2 <=1:
      x = 1
      while x <10:
            print(x)
            x = x+3
            print('Hit!')
if x == 10:
      print('voce matou!')
if question2 >=2:
      print('proseguindo...')
print('----------------------------------------------------')
question3 = int(input('deseja ir para longe da sua casa?:'))
if question3 <=1:
      print('voce esta perdido e esta sem abrigo, tem certeza de que quer continuar?:')
if question3 >=2:
      print('ok, mas voce acabou de encontrar um tesouro no lugar onde iria')
print('---------------------------------------------------------------------')
pygame.quit()


      


