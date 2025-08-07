"""Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

nome = input('Digite o seu nome: ')
while len(nome)<3:
    print('Nome inválido! Regidite o nome')
    nome = input('Digite o seu nome: ')

idade = int(input('Digite a idade: '))
while idade < 0 or idade>150:
    print('Idade inválido! Redigite a idade.')
    idade = int(input('Digite a idade: '))

sexo = input('Digite o sexo [f/m] ')
sexo.lower() #coloca o que o usuário digitou em minúsculo
while sexo != 'f' and sexo != 'm':
    print('Sexo inválido! Redigite o sexo')
    sexo = input('Digite seu sexo [f/m]')

salario = float(input('Digite o seu salário: '))
while salario < 1:
     print('Salário inválido, digite novamente.')


estado_civil = input('Digite seu estado civil: ').lower()
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Estado civil inválido! tente novamente.')
    estado_civil = input('Digite seu estado civil: ')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Sexo: {sexo}')
print(f'Salário: {salario}')
print(f'Estado civil: {estado_civil}')
