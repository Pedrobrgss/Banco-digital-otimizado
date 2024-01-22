import os
import time
import textwrap

def menu():
    menu =  """
                   
                          BANCO DIGITAL
  
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo usuario
    [nc] Nova conta
    [lc] Listar conta
    [q]  Sair
    
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito concluido com sucesso! seu saldo foi atualizado.")

    else:
        print("Não é possivel depositar este valor! tente novamente.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Não será possivel sacar por falta de saldo!")

    elif excedeu_limite:
        print("Operação falhou! o valor do saque excede o limite")  

    elif excedeu_saques:
        print("Você ultrapassou o limite de saques diários!")

    elif valor > 0: 
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        saldo -= valor
        print("Valor sacado com sucesso!")

    else:
        print("Operação falhou! o valor informado é inválido.")
    return numero_saques, saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações!" if not extrato else extrato)
    print(f"Saldo: R$ {saldo}")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuario com este CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,"endereco":endereco})

    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado, fluxo de criação de contas encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Âgencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        print("========".center(60,"="),end=" ")
        opcao = menu()
        if opcao == "d":
            os.system("cls")
            print("Depósito".center(60,"="))
            print()
            valor = float(input("Digite o valor que será o valor depositado:  "))

            saldo, extrato = depositar(saldo, valor, extrato) 

            print()
            print("========".center(60,"="))
            print("Voltando para o menu...")
            time.sleep(3)
            os.system("cls")

        elif opcao == "s":
            os.system("cls")
            print("Saque".center(60,"="))
            valor = float(input("Digite o valor que será sacado: "))

            numero_saques, saldo, extrato = sacar(saldo = saldo, valor= valor, extrato= extrato, limite= limite, numero_saques=numero_saques, limite_saques= LIMITE_SAQUES)

            print("========".center(60,"="))
            print("Voltando para o menu...")
            time.sleep(3)
            os.system("cls")

        elif opcao == "e":
            os.system("cls")
            print("Extrato".center(60,"="))
            print()

            saldo, extrato = exibir_extrato(saldo, extrato = extrato)
            print("========".center(60,"="))
            print("Voltando para o menu...")
            time.sleep(5)
            os.system("cls")

        elif opcao == "nu":
            os.system("cls")
            print("Novo usuario".center(60,"="))
            print()
             
            criar_usuario(usuarios)

            print("========".center(60,"="))
            print("Voltando para o menu...")
            time.sleep(5)
            os.system("cls")

        elif opcao == "nc":
            os.system("cls")
            print("Novo usuario".center(60,"="))
            print()

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

            print("========".center(60,"="))
            print("Voltando para o menu...")
            time.sleep(5)
            os.system("cls")

        elif opcao == "lc":
            listar_contas(contas)

            print("========".center(60,"="))
            print("Voltando para o menu...")
            time.sleep(5)
            os.system("cls")

        elif opcao == "q":
            break
            
        else:
            print("Operação inválida! selecione uma opção válida.")

main()