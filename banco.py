
menu= """Bem vindo ao Sistema Bancario!
Selecione uma das opções a baixo :

[D]Deposito ,[S]Saque ,[E]Extrato ,[Q]Sair

==>"""

saldo = 0.0
limite = 500
extrato= "================EXTRATO===================\n" 
numero_saque= 0
LIMITE_SAQUE = 3
movimentacao= 0

def historico(operacao):
    global extrato
    global movimentacao 
    movimentacao+= 1 
    extrato += f'{movimentacao} - {operacao}'
    print(extrato)

def depositar():
    global saldo
    while True:
        valor = float(input('digite uma valor para Deposito:\n==>'))
        if valor > 0:
            saldo += valor
            operacao = f" Operação de Deposito : \n valor : R$ {valor:.2f} \n Saldo : {saldo:.2f} .\n--------------------------------\n\n"
            historico(operacao)
            break
        else:
            print('valor não compativel , tente novamente!!!')

def sacar():
    global saldo 
    global limite
    global numero_saque
    global LIMITE_SAQUE
    while True:
        valor = float(input(f'DIgite um valo para saque inferior a saldo de  R$ {saldo:.2f} :\n ==>'))
        if (valor <= saldo) and (numero_saque < LIMITE_SAQUE) and (valor > 0) and (valor <= limite) :
            saldo -= valor
            numero_saque+= 1
            operacao = f" Operação de saque : \n valor : R$ {valor:.2f} \n Saldo : {saldo:.2f} .\n--------------------------------\n\n"
            historico(operacao)

            break
        elif valor > saldo :
            print(f'voce so tem R${saldo:.2f} de saldo tente novamente :')
        elif numero_saque >= (LIMITE_SAQUE):
            print('Limite diario de saque excedido:')
            break
        elif valor > limite:
            print(f'valor maior que o limite diario de R$ {limite:.2f}!')
        else:
            print('valor invalido tente novamente!!')




while True:
    opcao= input(menu).upper()

    if opcao == 'D':
        depositar()
    elif opcao == 'S':
        sacar()
    elif opcao == 'E':
        print("================EXTRATO===================\nNão forma realizadas movimentaçãos.\n\n\n" if (extrato == "================EXTRATO===================\n") else extrato)
    elif opcao == 'Q':
        break
    else :
        print('Opção invalida tente novamente')
