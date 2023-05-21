nome = "mailon cesar"
altura = 1.56
peso = 66
imc = peso / altura**2

linha_1 = f"{nome} tem {altura:,.2f} de altura "
linha_2 = f"pesa {peso} quilos e seu imc é"
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

# (f) chamado de f string
# print(nome, 'tem', altura, 'de altura,',)
# print('pesa', peso, 'quilos e seu imc é',)
# print("%.4f" % imc)