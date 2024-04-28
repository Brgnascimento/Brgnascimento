
def menu():
    menu = """
    ======== BEM VINDO AO CTBANK ==========

    Por favor, selecione a opção desejada!

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    => """
    return input(menu)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques>=limite_saques

    if excedeu_saldo:
            print(f'Saldo insuficiente. Seu saldo disponível é de: R$ {saldo}')

    elif excedeu_limite:
            print(f"Valor de saque excede o limite de R$ {limite}")

    elif excedeu_saques:
            print(f"Você execedeu o limite de  saques diários!")

    elif valor > 0:
            saldo -= valor 
            extrato +=f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1  
            print("\nSaque realizado com sucesso!")
    else:
            print("O valor informado é inválido!")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0 :

            saldo += valor

            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    else:
        print("O valor informado é inválido!")

    return saldo, extrato


def exibir_extrato(saldo,/,*,extrato):
    print("Extrato ".center(40,"="))
    print("\n Nenhuma movimentação foi realizada!\n" if not extrato else extrato)
    print(f"Saldo: {saldo:.2f}\n")
    print("========================================")
     
def criar_usuario(usuarios):
     cpf= input("Informe seu CPF (somente números): ")
     usuario =  filtrar_usuario(cpf, usuarios)

     if usuario:
        print("\n Já existe usuário com o mesmo CPF!")
        return
     nome = input("Informe o seu nome completo: ")
     data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
     endereco=input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

     usuarios.append({"nome": nome, "Data de nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})
     print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados=[usuarios for usuarios in usuarios if usuarios["cpf"]== cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None
     
def criar_conta(agencia, numero_conta, usuarios):
     cpf= input("Informe seu CPF (somente números): ")
     usuario =  filtrar_usuario(cpf, usuarios)
     if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
     
     print("Usuário não encontrado!")

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agência:{conta['agencia']}
          C/C:{conta['numero_conta']}
          Titular: {conta['usuario']['nome']}
          """
          print("=" * 100)
          print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios=[]
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Por favor, insira o valor do depósito: "))
            saldo, extrato= depositar(saldo, valor, extrato)    
            

        elif opcao == "s":
            valor = float(input("Insira o valor a ser sacado: "))
            saldo, extrato = sacar(
                  saldo=saldo,
                  valor=valor,
                  extrato=extrato,
                  limite=limite,
                  numero_saques=numero_saques,
                  limite_saques=LIMITE_SAQUES,
            )


        elif opcao == "e":
             exibir_extrato(saldo,extrato=extrato)

        elif opcao == "nu":
             criar_usuario(usuarios)

        elif opcao == "nc":
             numero_conta = len(contas)+1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)
             if conta:
                  contas.append(conta)
        
        elif opcao == "lc":
             listar_contas(contas)


        elif opcao == "q":
            break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
main()
