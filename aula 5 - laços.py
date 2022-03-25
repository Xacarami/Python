nomes = ['Renatão', 'Juliona', 'Papas na Língua', "Curupira"]

'''
for x in nomes:
    print(x)

print("")
'''
        #apenas demonstrativo, e não é recomendado fazer desta maneira
'''
for i in range(4):
    print(nomes[i])
'''

        #agora o mais recomendado, pois caso precise adicionar ou remover nomes, você poderá

for i in range(len(nomes)):
    print(nomes[i])

