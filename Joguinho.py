print('************************************')
print("Bem vindo ao joguinho de adivinhação")
print('************************************')

numeroSecreto = 23
totalDeTentativas = 3


for rodada in range(1, totalDeTentativas + 1):
    print("Tentativa {} de {}".format(rodada, totalDeTentativas))
    chute_str = input("Digite um numero de 1 a 25: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Coé meu nobre! avisei para colocar de 1 a 25. Punição -1 rodada')
        continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if acertou:
        print('Você é o mais brabo de konoha')
        break
    else:
        if maior:
            print('Você errou tio! o numero esta maior')
        elif menor:
            print('Você errou tio! o numero esta menor')

print('End Game')
