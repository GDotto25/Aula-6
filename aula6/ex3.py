"""Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

nome = input('Digite o seu nome: ')
# entrada nome
#validação do nome
while len(nome)<3:
    nome = input('Digite o seu nome: ')
#entrada idade
idade = int(input('Digite a idade [0 - 150]'))
#validação da idade
while idade < 0 or idade>150:
    idade = int(input('Digite a idade [0 - 150]')) 
    print(f'Sua idade é: {idade}')



