print("********************************")
print("Bem vindo ao jogo da Adivinhação")
print("********************************")

numero_secreto = 35
total_tentativas = 3
rodada = 1

while (total_tentativas >= rodada):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        rodada = total_tentativas
    elif maior:
        print("Você errou! O seu chute foi maior do que o número secreto")
    elif menor:
        print("Você errou! O seu chute foi menor do que o número secreto")

    rodada += 1

print("Game Over!")