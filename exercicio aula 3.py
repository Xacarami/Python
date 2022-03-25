'''
EXERCÍCIO:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter 18 anos ou mais
pesar mais ou igual a 60 quilos
e medir mais ou igual 1.70 metros
'''

idade = int(input("Digite  sua idade: "))
peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print("Você está apto para servir ao exército!")
else:
    print("Você não está apto para servir ao exército")