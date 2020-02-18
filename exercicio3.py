import random
menor_numero= int(input('Digite o menor valor: '))
maior_numero= int(input('Digite o maior valor: '))
qtde_valores= int(input('Digite quantos itens deseja na lista: '))
lista = random.sample(range(menor_numero,maior_numero), qtde_valores)
max(lista)
min(lista)
print(lista)