"""Faça um programa que leia um nome de usuário
 e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações."""
while True:
    login = input('Digite o Login: ')
    senha = input('Digite a senha: ')
    if senha == login:
        print('Senha inválida, tente novamente.')
    else:
        print('Cadastro feito com sucesso.')
        break