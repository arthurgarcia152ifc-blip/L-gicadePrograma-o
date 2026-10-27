maior_idade = 0

for i in range(1,6):
    idade = int(input("Digite sua idade:"))
    if idade > maior_idade:
        maior_idade = idade

print("Pessoa mais velha tem :",maior_idade," anos")