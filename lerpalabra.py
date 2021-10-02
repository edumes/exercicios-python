nome = str(input('digite uma palavra: ')).strip()
print('sua palavra em CAPS LOCK: {}'.format(nome.upper()))
print('sua palavra tem {} letras'.format(len(nome)))
separa = nome.split()
print('seu nome separado a cada espaço --> {}  '.format(separa))

