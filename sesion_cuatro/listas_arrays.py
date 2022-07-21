#listas simples.

from turtle import color


smartphone = ['xiaomi', 'iphone', 'samsung', 'motorola']

print(smartphone[1])


#listas con numeros negativos
paises = [
'AFGANISTÁN', 'ALBANIA', 'ALEMANIA', 'ANDORRA', 'ANGOLA', 'ANTIGUA  BARBUDA', 'ARABIA SAUDÍ', 'ARGELIA', 'ARGENTINA', 
'ARMENIA', 'ARUBA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIYÁN', 'BAHAMAS', 'BAHRÉIN', 'BANGLADESH', 'BARBADOS', 'BELARRÚS',
'BELICE', 'BENÍN', 'BOLIVIA', 'BOSNIA-HERZEGOVINA', 'BOTSUANA', 'BRASIL', 'BRUNÉI', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
'BUTÁN', 'BÉLGICA']

print ("el ultimo elemento de la lista es " + paises[-1])


#eliminar elementos utilizando el del[] y .remove()
hardware = ['case', 'motherboard', 'HDD', 'SSD', 'CPU', 'graphig card', 'RAM', 'power supply']

    #del hardware[-4]
hardware.remove('CPU')

print(hardware)


#insertar datos a una lista con append() e insert()
colores = ['rojo', 'azul', 'amarillo', 'verde', 'gris', 'morado', 'negro', 'blanco']

    #colores.append('naranja')
colores.insert(-1,'naranja')

print(colores)


