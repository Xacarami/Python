numero_convidados = int(input("Quantas pessoas será convidadas para a festa?: "))

lista = []
i = 0

for convidado in range(numero_convidados):
    i += 1
    lista.append(input("Qual o nome do convidado #"+ str(i) +"?: "))

for convidado in range(numero_convidados):
    print(lista[convidado])

print("fim da lista")