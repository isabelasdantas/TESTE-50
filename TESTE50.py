soma = 0
cont = 0
for c in range(1, 7):
    escolha = int(input('Escolha o {} número inteiro: '.format(c)))
    if escolha % 2 == 0:
        soma += escolha
        cont += 1
print('Você informou {} número PARES e a soma deles é {}.'.format(cont, soma))
