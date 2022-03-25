'''
EXERCÍCIO: Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso, o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''

numero_convidados = int(input("Quantas pessoas serão convidadas?: "))

i = 0
lista = []

for convidado in range(numero_convidados):
    lista.append(input("Qual o nome do convidado?: "))
print("")

for convidado in range(numero_convidados):
    while True:
        if i == numero_convidados:
            break
        print(lista[i])
        i += 1

print("\nFim da lista")