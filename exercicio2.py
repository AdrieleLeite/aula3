dicionario = {1: 'Domingo', 2: 'Segunda', 3: 'Terça' , 4: 'Quarta' , 5: 'Quinta' , 6: 'Sexta', 7: 'Sabado'}
usuario= int(input('Digite um numero entre 1 e 7: '))
if usuario < 8:
  print(dicionario[usuario])
else:
    print('Nada foi encontrado')

