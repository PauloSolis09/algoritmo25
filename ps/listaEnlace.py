def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
print ("Introduzca un numero entero: ")
num1 = int(input())
result=recursive_sum(num1)
print("El resultado es: ", result)