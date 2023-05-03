

"""
rep=int(input('ingresar repeticiones: '))
cantprimos=0
for i in range(rep):
    n=int(input('ingresar numero a verificar: '))
    if primo(n)==True:
        cantprimos=cantprimos+1
        print('es primo')
    else:
        print('no es primo')
print()
print(cantprimos)"""



import random

#primos


def primo(n):
    div=1
    cantidivisores=0
    while div<=n:
        if n%div==0:
             cantidivisores=cantidivisores+1
             div=div+1
        else:
            div=div+1
    if cantidivisores<=2:
        return True
    else:
        return False



#algoritmo de las cartas
#palos: 1-oro - 2-basto - 3-espada - 4-copa

anchosespada=0
cincooro=0
tiradas=int(input('ingresar la cantidad de tiradas'))
cantprimos=0

for i in range(tiradas):
    
    palo=random.randint(1,4)
    
    if primo(palo)==True:
        cantprimos=cantprimos+1
        print(palo, 'es primo', '' )
    else:
        print(palo, 'no es primo', '' )
    
    valor=random.randint(1,12)
    if primo(valor)==True:
        cantprimos=cantprimos+1
        print(valor, 'es primo', '')
    else:
        print(valor, 'no es primo', '')

    if palo==3 and valor==1:
        anchosespada=anchosespada+1
        
    if palo==1 and valor==5:
        cincooro=cincooro+1
        
print('la cantidad de anchos de espada que salieron fue: ', anchosespada)
print('la cantidad de 5 de oro que salieron fue :', cincooro)
print('la cantidad de primos es: ', cantprimos)











