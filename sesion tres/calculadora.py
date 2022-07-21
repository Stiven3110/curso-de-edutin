num1=int(input("introduce tu primer numero: \n"))
num2=int(input("introduce tu segundo numero: \n"))
opcion= 0
while True:
    print ('''  que hacer?
    1) sumar
    2)restar
    3)multiplicar
    4)dividir
    5)cambiar
    6)apagar
    ''')
    opcion = int(input("elige una opcion:\n"))
    if opcion ==1:
        print("")
        print("resultado: la suma de ",num1,"+",num2,
              "es igual a ",num1+num2)
    elif opcion ==2:
        print("")
        print("resultado: la resta de ", num1, "-", num2,
              "es igual a ",num1-num2)
    elif opcion ==3:
        print("")
        print("resultado: la multiplicacion de ", num1, "*", num2,
        "es igual a ", num1 * num2)
    elif opcion == 4:
        print("")
        print("resultado: la divicion de ", num1, "/", num2,
        "es igual a ", num1 / num2)
    elif opcion == 5:
        num1 = int(input("introduce tu primer numero: \n"))
        num2 = int(input("introduce tu segundo numero: \n"))
    elif opcion == 6:
        break
    else:
        print("opcion incorrecta")

