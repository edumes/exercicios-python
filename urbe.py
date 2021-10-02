distancia = int(input('digite a distancia: '))
if distancia <= 200:
      preço = distancia * 0.50
else:
      preço = distancia * 0.45
print('o preço da sua passagem sera de  {:.2f}'.format(preço))
