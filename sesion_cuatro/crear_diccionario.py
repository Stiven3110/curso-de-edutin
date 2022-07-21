#Diccionario

Equipo = {10:"Paulo Dybala",11:"Douglas costa",7:"Cristiano Ronaldo",17:"Mario Mandzukic"}

print(Equipo.get(8,"no existe un jugador con ese dorsal")) #(nota para cuando no se encuentre un elemento)
print(12 in Equipo) #(busqueda directa del dorsal de un jugador)
print(Equipo.keys()) #(mostrar claves de los jugadores (dorsales))
print(Equipo.values()) #(nombre de los jugadores)
print(Equipo.items()) #(nombre y valor de cada jugador)
print(len(Equipo)) #(totalidad de jugadores en el diccionario)
Equipo.clear() #(limpiar el diccionario)

print(Equipo)