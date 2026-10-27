secreto = 42
tentativas = 0
resposta = 0

while tentativas < 3:
    resposta = int(input("Qual a sua escolha: "))
    if resposta == secreto:
        break
    else:
        tentativas += 1

if resposta == secreto:
    print("VOCÊ ACERTOU")
else:
    print("Game Over")