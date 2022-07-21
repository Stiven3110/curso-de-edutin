#listas 

frutas = ['Papaya','Sandía','Naranjas','Manzanas','Melón','Piña','Limón','Peras','Kiwi','Uvas','Tamarindo','Toronjas']
print(frutas)

i = input("escriba el nombre de la fruta\n")
opcion=0
while True:
    print('''que hacer?
    1)agregar
    2)eliminar
    3)cambiar
    4)terminar
    ''')
    opcion = int(input("elige una opcion:\n"))
    if opcion ==1:
        frutas.append(i)
        print("ha sido agregado a la lista",frutas)
    elif opcion ==2:
        frutas.remove(i)
        print("la fruta ha sido eliminada", frutas)
    elif opcion ==3:
        i = int(input("elija una opcion: \n"))
    elif opcion == 6:
        break
    else:

        print("opcion incorrecta")

