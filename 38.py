soma_total = 0
soma_atual = float(input("Qual o valor do produto: "))
while soma_atual != 0:
    soma_total += soma_atual
    soma_atual = float(input("Qual o valor do produto (ou 0 para finalizar): "))

print("Valor total: ",soma_total)
