entrada = input('digite um horario: ')
 
try:
    hora = int(entrada) 

    if hora >= 0 and hora <= 11:
        print('bom dia')
    
    elif hora >= 12 and hora <= 17:
        print('boa tarde')

    elif hora >= 18 and hora <= 23:
        print('boa noite')
    else:
        print('não conheço essa hora')

except:
    print('por favor digite numeros inteiros')
