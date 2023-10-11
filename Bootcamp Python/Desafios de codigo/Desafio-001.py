menu = """
[1] Depósito
[2] Extrato
[3] Saque
[4] Sair
==> """

saldo = 0
limite = 500
extrato = ' '
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Qual valor você deseja depositar? '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Informe um valor válido!')

    elif opcao == 2:
        print('\n########## Extrato ##########')
        print('Nenhuma operação foi registrada.' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}' )
        print('###############################')

    
    elif opcao == 3:
        valor = float(input('Quanto você deseja sacar? '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('A operação falhou, seu saldo é insuficiente. ')

        elif excedeu_limite:
            print('Seu limite de saque, e de: R$ 500. ')

        elif excedeu_saque:
            print('Volte amanhã, seu limite de operações foi excedido. ')

        elif valor > 0:
            saldo -= valor
            extrato += f' Saque: {valor:.2f}\n'
            numero_saque += 1

        else:
            print('Operação falhou, o valor informado é inválido.')


    elif opcao == 4:
        
        break

    else:
        print('Por favor, digite uma opção válida.')