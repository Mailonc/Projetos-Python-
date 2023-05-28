"""
Flag (Bandeiratipo) - Marcar um local
none = não valor
is e is not = é ou não (tipo , valor , indentidade )
id = indentidade  
"""
# V1 = 'a'
# V2 = 'b'
# print(id(V1))
# print(id(V2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print( 'faça algo')
else:
     print('não faça algo')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
     print('não passou no if')
 
if passou_no_if is not None:
     print('passou no if')