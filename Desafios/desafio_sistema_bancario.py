menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Por favor, insira o valor do depósito: "))

        if valor > 0 :

            saldo += valor

            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido!")
        
        

    elif opcao == "s":
        valor = float(input("Insira o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques>=LIMITE_SAQUES

        if excedeu_saldo:
            print(f'Saldo insuficiente. Seu saldo disponível é de: R$ {saldo}')

        elif excedeu_limite:
            print(f"Valor de saque excede o limite de R$ {limite}")

        elif excedeu_saques:
            print(f"Você execedeu o limite de {LIMITE_SAQUES} saques diários!")

        elif valor > 0:
            saldo -= valor 
            extrato +=f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1  
        else:
            print("O valor informado é inválido!")    




    elif opcao == "e":

        print(" Extrato ".center(40,"="))

        print("\n Nenhuma movimentação foi realizada!\n" if not extrato else extrato)

        print(f"Saldo: {saldo:.2f}\n")

        print("========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
