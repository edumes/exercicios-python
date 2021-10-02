print('===== tabelinha daa burguesia =====')
pontos_first = 0
#-------------------------------------------------------
q1 = str(input("vc tem netflix: "))
if q1 == 'sim':
    pa = pontos_first + 10 #pa -> pontos atuais
    print('vc esta com {} pts'.format(pa))
if q1 == 'nao':
    pa2 = pontos_first + 0 #pa2 -> pontos atuais 2.0
    print('vc esta com {} pts'.format(pa2))
if q1 == 0:
    print('pontos totais: 0')
else:
    print('pontos totais 10')
#-------------------------------------------------------
pontos_sec = pontos_first
q2 = str(input('vc estuda em escola particular?: '))
if q2 == 'sim':
    pa3 = pontos_sec + 10
    print('vc esta com {} pts'.format(pa3))
if q2 == 'nao':
    pa3 = pontos_sec + 0
    print('vc esta com {} pts'.format(pa3))
#-------------------------------------------------------


    
    


         
    
