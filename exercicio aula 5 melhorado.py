'''
EXERCÍCIO: Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso, o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''

print("\nPROGRAMA MEDIOCRE DE CONVIDADOS")
print("+++++++++++++++++++++++++++++++")

numero_convidados = int(input("Quantas pessoas serão convidadas?: "))

i = 0
lista = []

for convidado in range(numero_convidados):
    i += 1
    lista.append(input("Qual o nome do convidado #"+ str(i) +"?: "))

print("\nSERÃO ENTÃO", numero_convidados, "CONVIDADO(S):")

for convidado in lista:
    print(convidado)

print("\nFim da lista")