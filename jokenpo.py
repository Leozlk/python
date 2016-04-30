# - Python
# Jokenpô!
# jokenpo.py - by Leonardo Rodrigues Silva - 2016
#
import random
j = ['pedra','papel','tesoura']
try:
    n = int(input('Quantas partidas gostaria de jogar? '))
    for i in range(n):
        print('-------------------------')
        v = str(input('pedra, papel ou tesoura? '))
        print('-------------------------')
        rnd_bot = random.choice(j)
        if v in ('pedra', 'papel', 'tesoura'):
            print("voce: "+v)
            print("oponente: "+rnd_bot)
        if v == 'papel' and rnd_bot == 'pedra':
            print('voce embrulhou a pedra do oponente!')
        if v == 'papel' and rnd_bot == 'tesoura':
            print('oponente cortou seu papel!')
        if v == 'pedra' and rnd_bot == 'tesoura':
            print('voce quebrou a tesoura do oponente!')
        if v == 'pedra' and rnd_bot == 'papel':
            print('oponente embrulhou sua pedra!')
        if v == 'tesoura' and rnd_bot == 'pedra':
            print('oponente quebrou sua tesoura!')
        if v == 'tesoura' and rnd_bot == 'papel':
            print('voce cortou o papel do oponente!')
        if v == rnd_bot:
            print('empate!')
        if v not in ('pedra', 'papel', 'tesoura'):
            print("opcao invalida")
except ValueError:
    print("favor, insira um valor valido")
