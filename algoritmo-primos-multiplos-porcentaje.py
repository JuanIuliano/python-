

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


"""
reps=int(input('ingresar repeticiones: '))

 for i in range(reps):
    n=int(input('ingrese numero: '))
    if multiplo(n)==True:
        print('el numero es multiplo de 2')
    else:
        print('no es multiplo de 2')"""

    
#multiplo2
def multiplo(n):
    if n%2==0:
        return True
    else:
        return False



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
cantmultiplos=0

for i in range(tiradas):
    
    palo=random.randint(1,4)   
    if primo(palo)==True:
        cantprimos=cantprimos+1
        print(palo, 'es primo', '' )
    else:
        print(palo, 'no es primo', '' )
    if multiplo(palo)==True:
        cantmultiplos=cantmultiplos+1
            
    
    valor=random.randint(1,12)
    if primo(valor)==True:
        cantprimos=cantprimos+1
        print(valor, 'es primo', '')
    else:
        print(valor, 'no es primo', '')
    if multiplo(valor)==True:
        cantmultiplos=cantmultiplos+1



    if palo==3 and valor==1:
        anchosespada+=1
        
    if palo==1 and valor==5:
        cincooro+=1
        
        porcentajeoro=cincooro*(100/80)
        
print('la cantidad de anchos de espada que salieron fue: ', anchosespada)
print('la cantidad de 5 de oro que salieron fue :',porcentajeoro,'%')
print('la cantidad de primos es: ', cantprimos)
print('la cantidad de multiplos de 2 es: ', cantmultiplos)













