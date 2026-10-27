soma_atual = input("Digite o numero para somar:")
soma_total = float(soma_atual)

while soma_atual != 0:
    soma_atual = float(input("Digite o numero para somar:"))
    soma_total = soma_total + soma_atual
    print("Soma até agora =", soma_total)

print("A soma total de ", soma_total)
