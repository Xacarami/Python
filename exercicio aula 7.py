'''
EXERCICIO: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa coleção
faça outra função que retorna o menor numero dessa coleção
'''

coleção = (0.25,0.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

def maior_numero(coleção):
    return max(coleção)

def menor_numero(coleção):
    return min(coleção)

print(maior_numero(coleção))

print(menor_numero(coleção))