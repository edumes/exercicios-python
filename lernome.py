nome = str(input('digite seu nome completo: ')).strip()
print('seu nome em maiusculas: {}'.format(nome.upper())) #.upper para deixar letras em maiusculas 
print('seu nome em minusculas: {}'.format(nome.lower())) #.lower deixa letras em minusculas
print('seu primeiro nome tem: {} letras ao todo'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem: {} letras'.format(nome.find(' ')))
separa = nome.split() #separa os nomes em listas
print(separa)
