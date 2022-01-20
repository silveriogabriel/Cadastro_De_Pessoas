'''
    PROGRAMA DE CADASTRO DE PESSOAS!
    
    Crie um programa que cadastre uma lista de pessoas com voucher, nome, email, Telefone, Curso
'''

#Importando modulos necessarios

from random import randint
from time import sleep

#Definindo pessoas

pessoas = []
vouchers = []

#Sistema de menus

def menu():
    print(f'**********MENU**********')
    print('''[ 1 ] - Nova Inscrição
[ 2 ] - Ver Inscriçoes.
[ 0 ] - Sair...''')
    while True:
        try:
            escolha = int(input('Digite sua escolha: '))
            if escolha > 2 or escolha < 0:
                raise()
        except:
            sleep(1)
            print('O valor digitado é invalido.')
        else:
            return escolha
            break

#Cadastrando novo usuario

def cadastro():
    while True:
        voucher = randint(0,999)
        if voucher in vouchers:
            voucher = randint(0,999)
        else:
            vouchers.append(voucher)
            break
    print('-'*28)
    print(f'Cadastrando usuario {voucher}')
    print('-'*28)
    nome = input('Digite seu nome: ').title()
    email = input('Digite seu E-mail: ')
    tel = input('Digite seu Telefone: ')
    curso = input('Digite seu Curso: ')
    dicionarioP = {
        'voucher': voucher,
        'nome': nome,
        'email': email,
        'telefone': tel,
        'curso': curso
    }
    pessoas.append(dicionarioP)
    print('-'*20)

#Lendo pessoas cadastradas

def lerpessoas():
    print('\nPROCESSANDO...')
    sleep(2)
    try:
        if not pessoas:
            raise
        print('----------Lista De Inscritos----------')
        for item in pessoas:
            for i,v in item.items():
                print(f'{i} : {v}')
            print('-' * 30)
            sleep(1)
    except:
        print('NENHUMA PESSOA CADASTRADA!\n')
            

#Inicio do programa

while True:
    escolha = menu()
    if escolha == 1:
        cadastro()
    elif escolha == 2:
        lerpessoas()
    elif escolha == 0:
        print('ENCERRANDO...')
        sleep(2)
        print('MUITO OBRIGADO POR ULTILIZAR O PROGRAMA...')
        break