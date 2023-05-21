"""
Introdução ao try / except
try -> tentar executar o código 
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('vou dobrar o numero que vc digitar: ')

if numero_str.isdigit(): 
 
 mumero_float = float(numero_str)
 print(f'o dobro de {numero_str} é {mumero_float * 2:.0f}')
else:
 print('isso nao é numero')