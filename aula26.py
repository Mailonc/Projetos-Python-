"""
formatação basica de strings
s - string
d - int 
f - float
.<numero de digitos>f
x ou x hexadecimal 
(caracteristicas)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
ex.:0>-100,.1f
conversion flags - ir !s !a 
"""
variavel = "ABC"
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}.')
print(f'{variavel:^10}.')
print(f'{1000.736373773373838:0=+10,.1f}')
print(f'o hexedecimal de 1500 é {1500:08x}')