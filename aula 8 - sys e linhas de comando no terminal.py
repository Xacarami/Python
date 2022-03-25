import sys  #importou uma biblioteca com funções e variáveis para o terminal

argumento = sys.argv    #tudo que for adicionado pelo terminal no argv, será colcoado no argumento, e será printado

'''
dentro do terminal:
primeiro critério: o que fará? Soma ou Subtração?
segundo critério: primeiro número
terceiro critério: segundo número
'''

def soma(n1, n2):
    return float(n1) + float(n2)    #float para não ter problemas caso ponha algum numero decimal

def sub(n1, n2):
    return float(n1) - float(n2)

if argumento[1] == "soma":
    resposta = soma(argumento[2], argumento[3])
elif argumento[1] == "sub":
    resposta = sub(argumento[2], argumento[3])
else:
    resposta = "Valor errado"

print(resposta)