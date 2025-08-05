#dontpad.com/pythonnoite
"""Faça um programa que peça uma nota, 
entre zero e dez. Mostre uma mensagem caso o valor seja
inválido e continue pedindo 
até que o usuário informe um valor válido."""
continua = True
while continua:
    nota = int(input('Digite uma nota entre [0 e 10]: '))
    if nota < 0 or nota > 10:
        print('Você digitou um valor inválido!')
    else:
        print('O valor digitado é válido.')
        continua = False
