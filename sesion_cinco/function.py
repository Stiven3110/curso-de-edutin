#funciones

def my_function(age, name = 'Stiven' ):
    print('Hola ' + name + 'your age is ' + str(age) + '!')

my_function(29, 'Stiven ' )

def sum_numbers(a, b):
    return a + b

sum = sum_numbers(29, 1)
print(sum)

def recursion(k):
    if (k > 0):
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

recursion(7)
