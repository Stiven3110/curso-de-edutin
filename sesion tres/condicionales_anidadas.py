#condicionales combinados
edad = int(input("digite su edad: "))

'''
#forma "larga" de utilizar la condicional
if edad >=18:
    print("es mayor de edad")
else:
    print("No es mayor de edad")
'''

#formas de utilizar los condicionales.
#if edad >0 and edad<100:
if 0<edad<100:
    print("edad correcta")
    if edad>=18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
else:
    print("edad incorrecta")