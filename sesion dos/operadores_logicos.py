'''
OPERADORES EN GENERAL
1.() resolver de adentro hacia afuera
2. ** exponeciacion
+,/,mod (modulo),not(negacion de variables)
4. +,-,and (adjuncion)
5.>,<,==,>=,<=,!=,or
'''

a = 10
b = 15
c = 20

#resultado = ((a<b)and (b<c))
#resultado = ((a>b)and(b<c))
#resultado = ((a>b) or (b<c))
resultado = not((a>b) or (b<c))

print(resultado)