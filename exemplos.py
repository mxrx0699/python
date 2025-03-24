# # compressão de lista
# # exemplo 1
# x = [1,2,3,4]
# y = []
# j = []
# for i in x:
#     y.append(i**2)
# print(y)

# # ==========
# w = [i**2 for i in x]
# print(w)

# # ============
# for i in x:
#     if i % 2 == 0:
#         j.append(i**2)
# # ====================
# j = [i for i in x if i % 2 == 0]
# print()

#enumeração de lista

lista = ['abacate', 'abacaxi', 'melão', 'ameixa', 'maçã']
for i in range(len(lista)):
    print(i, lista[i])
    
# A função enumerate() em Python é usada para iterar sobre uma sequência como uma lista, tupla ou string e obter tanto o índice (posição) quanto o valor de cada item da sequencia ao mesmo tempo.
for i, nome in enumerate(lista):
    print(i,nome)