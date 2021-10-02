num = int(input('digite um numero: '))
print('''escolha o metodo de conversão:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter paar hexadecimal''')
opçao = int(input('sua opçao: '))
if opçao == 1:
      print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
      print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
      print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
      print('opçao invalida! tente outra vez.') 
