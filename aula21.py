# operadores logicos 
# and (e) or (ou) not (não)
# and - todas as condições precisam ser 
# verdadeiras.
# se qualuqe valor fot considerado falso,
# a expressão inteira será avaliada naquela valor
# são considerados falsy (que vc ja viu)
# 0 0.0 "" false 
# também exite o tipo none que é 
# usando para representar um não valor 
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('senha: ')
# if True:

# senha_permitida = '123456'
# if entrada == "E" and senha_digitada == senha_permitida:
  #  print('Entrar')

# else:
#... print('sair')
# avaliação de curto circuito
print(True and True and True)
print(True and 0 and True) 
 
if 0 and 1:
 print(True and 1)
  
if 1 and 1:
 print(True and 1 and False) 
