import random
numero = random.randint(1, 1000)
tentativas = 0

while tentativas < 10:
 chute = int(input("Adivinhe o número: "))
 if chute == numero:
    print ("Parabéns, você acertou o número com " + tentativas + "tentativas!")
 elif chute > numero:
    print ("Errou, o numero é menor.")
 else:
    print ("Errou, o número é maior.")
 tentativas += 1
if chute != numero:
    print("Suas tentativas acabaram.")
