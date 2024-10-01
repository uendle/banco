from datetime import datetime , time
menu= """Bem vindo ao Sistema Bancario!
Selecione uma das opções a baixo :

[D]Deposito ,[S]Saque ,[E]Extrato ,[CU]Cadastrar Usuario ,[CC]Criar Conta[Q]Sair

==>"""
lista_cadastro = ["CPF" ,"nome","data de nascimento","rua","numero","bairro","cidade"]
dicionario_de_usuarios = {}
dicionario_log={}

def gravar_log(cpf,log,mensagem):
    dicionario = {}
    dicionario[log]= mensagem
    dicionario_log[cpf]=dicionario

def criar_log(operacao ,cpf):
    if operacao == 'CU':
        data= datetime.strftime(datetime.now(),'%d/%m/%Y')
        log= datetime.strftime(datetime.now(),f'CU%d%m%Y-%H%M%S')
        tipo= 'Criar Usuario'
        mensagem=f'\nLog: {log}\nData: {data}\nOperação: {tipo}\n'
        gravar_log(cpf,log,mensagem)
        
    elif operacao == 'Cc':
        data= datetime.strftime(datetime.now(),'%d/%m/%Y')
        log= datetime.strftime(datetime.now(),f'CC%d%m%Y-%H%M%S')
        tipo= 'Criar conta'
    elif operacao == 'D':
        data= datetime.strftime(datetime.now(),'%d/%m/%Y')
        log= datetime.strftime(datetime.now(),f'DE%d%m%Y-%H%M%S')
        tipo= 'Deposito'
    elif operacao == 'S':
        data= datetime.strftime(datetime.now(),'%d/%m/%Y')
        log= datetime.strftime(datetime.now(),f'SA%d%m%Y-%H%M%S')
        tipo= 'Saque'
    else:
        print('operação nao identificada.')



def deposito():#apenas argumentos por posição
    cpf= input('digite seu cpf:')
    if cpf in dicionario_de_usuarios:
        conta=int(input('digite o numero de sua conta:'))
        if conta in dicionario_de_usuarios[cpf]['contas']:
            if dicionario_de_usuarios[cpf]['contas'][conta] == 0.0:
                valor= float(input('Digite uma valor:'))
                dicionario_de_usuarios[cpf]['contas'][conta]= valor
                criar_log(operacao='D',cpf=cpf)
            else:
                valor= float(input('Digite uma valor:'))
                dicionario_de_usuarios[cpf]['contas'][conta]+= valor
                #criar_log(operacao='D',cpf=cpf)
        else:
            input('Conta inexistente!!!')
    else:
        input('usuario não cadastrado!')

def saque():#so recebe argumentos apenas nomeados
    cpf= input('digite seu cpf:')
    if cpf in dicionario_de_usuarios:
        conta=int(input('digite o numero de sua conta:'))
        if conta in dicionario_de_usuarios[cpf]['contas']:
            valor= float(input('Digite uma valor:'))
            if dicionario_de_usuarios[cpf]['contas'][conta] == 0.0 or  dicionario_de_usuarios[cpf]['contas'][conta] < valor:
                input(f'Lamento seu saldo atual esta {dicionario_de_usuarios[cpf]['contas'][conta]} !!!')
            else:
                dicionario_de_usuarios[cpf]['contas'][conta]-= valor
                #criar_log(operacao='S',cpf=cpf)
        else:
            input('Conta inexistente!!!')
    else:
        input('usuario não cadastrado!')

def criar_conta():#pode ter mais de uma conta,
    cpf = input('Digite seu cpf :\n==>')
    dicionario_contas = {}

    if cpf in dicionario_de_usuarios:
        if 'contas' in dicionario_de_usuarios[cpf]:
            dicionario_contas = dicionario_de_usuarios[cpf]['contas']
            conta= len(dicionario_contas.keys()) + 1
            print(conta)
            dicionario_contas[conta]= 0.0
            dicionario_de_usuarios[cpf]['contas']= dicionario_contas
            #criar_log(operacao='CU',cpf=cpf)
            input(f'conta {conta} cadastrada com sucesso !\nClique em qualquer tecla para continuar.')

        else:
            dicionario_contas[1]= 0.0
            dicionario_de_usuarios[cpf]['contas']=dicionario_contas
            input(f'conta {1} cadastrada com sucesso !\nClique em qualquer tecla para continuar.')
            #criar_log(operacao='CU',cpf=cpf)

    else:
        input('Cadastre um usuario antes de abrir um aconta: ')

def cadastrar_usuario():
    print("Bem vindo ao sistema de cadastro :")
    dicionario_de_um_usuario={}
    for i in lista_cadastro:
        dado= input(f'digite seu {i} :\n==> ')
        dicionario_de_um_usuario[i]= dado
        dicionario_de_usuarios[dicionario_de_um_usuario['CPF']] = dicionario_de_um_usuario
        if i == 'CPF':
            criar_log('CU',dado)
    




while True:
    opcao = input(menu).upper()

    if opcao == 'CU':  
        cadastrar_usuario()
        #print(dicionario_log)
    elif opcao == 'CC':
        pass
    elif opcao == 'D':
        pass
    elif opcao == 'S':
        pass
    elif opcao == 'Q':
        break
    else:

        print('valo nao suportado:')