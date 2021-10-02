peso = float(input('qual é o seu peso? (Kg): '))
altura = float(input('qual é sua altura? (m): '))
imc = peso / (altura ** 2)
print('o imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
      print('vc esta abaixo do peso normal')
elif 18.5 <= imc 25:
      print('vc esta na faixa do peso norma,parabens')
elif 25 <= imc < 30:
      print('vc esta em sobrepeso')
elif 30 <= imc 40:
      print('vc esta em obesidade, cuidado')
elif imc >= 40:
      print('vc esta em obesidade morbida')
