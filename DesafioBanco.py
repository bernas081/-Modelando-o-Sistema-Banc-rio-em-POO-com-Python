import textwrap


def menu():
    menu = """
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair
    => """
    return input(textwrap.dedent(menu))


# ================= FUNÇÕES BANCÁRIAS =================

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Valor inválido!")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n Saldo insuficiente!")

    elif valor > limite:
        print("\n Valor excede o limite!")

    elif numero_saques >= limite_saques:
        print("\n Limite de saques atingido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")

    else:
        print("\nValor inválido!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


# ================= USUÁRIOS =================

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = input("CPF: ")

    if filtrar_usuario(cpf, usuarios):
        print("Este usuário já existe!")
        return

    nome = input("Nome: ")
    nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "nascimento": nascimento,
        "endereco": endereco
    })

    print("Usuário criado!")


# ================= CONTAS =================

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado!")
        return None

    print("Conta criada com sucesso!")
    return {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario
    }


def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero']}")
        print(f"Titular: {conta['usuario']['nome']}")


# ================= MAIN =================

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    LIMITE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            try:
                valor = float(input("Valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
            except:
                print(" Entrada inválida!")

        elif opcao == "2":
            try:
                valor = float(input("Valor do saque: "))
                saldo, extrato, numero_saques = sacar(
                    saldo, valor, extrato, LIMITE, numero_saques, LIMITE_SAQUES
                )
            except:
                print("Entrada inválida!")

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


main()