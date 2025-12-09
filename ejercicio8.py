""""
Escribir una función es_primo(num) que reciba un número entero y devuelva True si es primo
y False si no lo es. Probar la función con varios números ingresados por el usuario
"""
#definir funcicones 
def es_primo(num) :
    
    if num % 2==0:
        return False
    if num < 2 :
        return False
    if num == 2:
        return True
    i=3
    while i * i <=num:
        if num % i == 0 :
            return False
        i +=2
    
    return True

#Iteracion con el usuario

while True :
    numero = int(input('Introducir un numero : '))
    
    if(es_primo(numero)) :
        print(f'El numero {numero} si es primo ')
        break
    else  :
        print(f'El numero {numero} no es primo , vuelva a intentarlo')
    
    

    
