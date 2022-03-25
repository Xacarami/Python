'''
EXERCICIO: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa coleção
faça outra função que retorna o menor numero dessa coleção
'''

lista = (0.1,0.5,1,2,3,4,5,6,7,8,9,16,32,64,1024,13456)

def maior(lista):
    maior_item = lista[0]
    for numero in lista:
        if numero > maior_item:
            maior_item = numero
    return maior_item

def menor(lista):
    menor_item = lista[0]
    for numero in lista:
        if numero < menor_item:
            menor_item = numero
    return menor_item


print(maior(lista))
print(menor(lista))