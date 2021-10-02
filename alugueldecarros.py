dias = int(input('quantos dias alugados?: '))
km = float(input('quantos kilometros percorreu?: '))
pago = (dias * 60) + (km * 0.15) 
print('total a pagar é {:.2f} reais'.format(pago))
