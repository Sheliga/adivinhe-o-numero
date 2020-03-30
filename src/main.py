# Essa é a implementação de um jogo de adivinhação de numeros.

import random



print('Olá, qual o seu nome?')
name = input()

numberMin = 0
numberMax = 20
secretNumber = random.randint(numberMin, numberMax)

print("Hm... %s, eu estou pensando em um numero entre %s e %s." % (name, numberMin, numberMax))


# Perguntar ao jogador um numero definido de vezes, por exemplo, se setar a função range como range(1,7)
# o jogador terá 6 tentativas com o range iniciando em 1 e indo até 7.

for guessesTaken in range(1, 7):
    print('Dê um palpite.')
    guess = int(input())
    if(guess < secretNumber):
        print('Você chutou muito baixo')
    elif(guess > secretNumber):
        print('Você chutou muito Alto')
    else:
        break

if(guess == secretNumber):
    print('Bom trabalho %s, você acertou o meu numero em %s tentativas.' % (name, guessesTaken))
else:
    print('Não, o número em que eu estava pensando era %s' % (secretNumber))