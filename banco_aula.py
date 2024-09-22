menu= '''

[D] Depositar
[S] Saque
[E] Extrato
[Q] Sair

==>'''

saldo= 0
limite= 500
extrato= "" 
numero_saque= 0
LIMITE_SAQUE= 3

while True:

    opcao= input(menu).upper()#elimino erro de case sensitive

    if opcao == "D":
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0 :
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"

        else:
            print('Operação falhou! Valor informado invalido.')

    elif opcao == 'S':
        valor= float(input('Informe o valor do Saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo :
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite :
            print('Operação falhou! Você Já excedu o seu limite.')

        elif excedeu_saque :
            print('Operação falhou! Você excedeu seu numero de saque.')

        elif valor > 0 :
            saldo-= valor
            extrato+= f'Saque: R$ {valor:.2f}\n'
            numero_saque+= 1

        else:
            print("Opçao falhou! O valor digitado e inválido.")

    elif opcao == "E":
        print("\n===================EXTRATO===================")
        print("Não forma realizadas movimentações." if not extrato else extrato)#if ternario 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")

    elif opcao == "Q":
        break

    else:

        print("Operação invalida por favor selecione novemente a opçao desejada.")