numeros_par = 0
numeros_impar = 0
for i in range(1,6):
    numeros = int(input("Escreva um numero: "))
    if int(numeros) % 2 == 0:
        numeros_par = numeros_par+1
    else:
        numeros_impar = numeros_impar+1

print("Numeros pares:",numeros_par)
print("Numeros impar:",numeros_impar)
