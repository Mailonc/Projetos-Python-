# operadores in e not in 
# strings são iteráveis 
# 0 1 2 3 4 5 
# O t á v i o 
#-6-5-4-3-2-1 
# nome = "otávio"
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero'in nome)
# print(10* '-')
# print('vio'not in nome)
# print('zero'not in nome)

nome = input('digite seu nome: ')
encontrar = input('digite o que deseha encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')