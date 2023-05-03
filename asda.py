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
print(cantprimos)
#numero maximo va a tener 2 divisores
#contador que pare cuando el divisor sea igual que el numero que queres dividir
