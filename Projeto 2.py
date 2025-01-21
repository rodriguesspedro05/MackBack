# Feito por Pedro Henrique de Almeida Rodrigues

# Armazenar informações da conta
conta = {
    "numero": None,
    "nome": None,
    "telefone": None,
    "email": None,
    "saldo": 0,
    "limite_credito": 0,
    "senha": None,
    "historico_operacoes": [],
    "bloqueado": False
}

# Função para obter entrada do usuário
def obter_entrada(mensagem):
    return input(mensagem)

# Funções de validação
def validar_nome(nome):
    return nome != ""

def validar_telefone(telefone):
    return telefone != ""

def validar_email(email):
    return email != ""

def validar_senha(senha):
    return len(senha) == 6 # Verifica se a senha tem 6 caracteres

def confirmar_senha(senha, repeticao_senha):
    return senha == repeticao_senha

# Função para obter saldo, validando se é um número válido
def obter_saldo(mensagem):
    while True:
        try:
            valor = float(obter_entrada(mensagem))
            if valor >= 0:
                return valor
            print("Valor inválido Deve ser um número maior ou igual a zero.")
        except ValueError:
            print("Valor inválido, deve ser um número.")

# Função para autenticar a conta, onde verifica se a conta está cadastrada e não está bloqueada
def autenticar_conta():
    if not conta["numero"]:
        print("Conta não cadastrada!")
        return False

    if conta["bloqueado"]:
        print("Conta bloqueada!")
        return False
# Solicita o número da conta e verifica se é válido
    numero_conta = obter_entrada("Informe o número da conta: ")
    if numero_conta != conta["numero"]:
        print("Número da conta incorreto!")
        return False

# Solicita a senha e verifica se é válida (até 3 tentativas)
    for _ in range(3):
        senha = obter_entrada("Informe a senha: ")
        if senha == conta["senha"]:
            return True
        print("Senha incorreta!")
    conta["bloqueado"] = True
    print("Conta bloqueada!")
    return False

# Função para cadastro de conta, verificando se esta conta já existe além de solicitar a validação de dados
def cadastrar_conta():
    if conta["numero"]:
        print("Conta já cadastrada!")
        return

    conta["numero"] = obter_entrada("Número da conta: ")
    conta["nome"] = obter_entrada("Nome do cliente: ")
    while not validar_nome(conta["nome"]):
        print("Nome do cliente não pode estar em branco!")
        conta["nome"] = obter_entrada("Nome do cliente: ")

    conta["telefone"] = obter_entrada("Telefone: ")
    while not validar_telefone(conta["telefone"]):
        print("Telefone não pode estar em branco!")
        conta["telefone"] = obter_entrada("Telefone: ")

    conta["email"] = obter_entrada("Email: ")
    while not validar_email(conta["email"]):
        print("Email não pode estar em branco!")
        conta["email"] = obter_entrada("Email: ")

    conta["saldo"] = obter_saldo("Saldo inicial: ")
    conta["limite_credito"] = obter_saldo("Limite de crédito: ")

    conta["senha"] = obter_entrada("Senha: ")
    while not validar_senha(conta["senha"]):
        print("Senha deve ter 6 caracteres!")
        conta["senha"] = obter_entrada("Senha: ")

    confirmar_senha_entrada = obter_entrada("Repita a senha: ")
    while not confirmar_senha(conta["senha"], confirmar_senha_entrada):
        print("Senhas não coincidem!")
        confirmar_senha_entrada = obter_entrada("Repita a senha: ")

    print("Cadastro realizado!")

# Função para depósito
def depositar():
    if not autenticar_conta():
        return

    valor_deposito = obter_saldo("Valor do depósito: ")
    while valor_deposito <= 0:
        print("Valor do depósito deve ser maior que zero!")
        valor_deposito = obter_saldo("Valor do depósito: ")

    conta["saldo"] += valor_deposito
    conta["historico_operacoes"] += [("depósito", valor_deposito)]
    print("Depósito realizado com sucesso!")

# Função para saque
def sacar():
    if not autenticar_conta():
        return

    valor_saque = obter_saldo("Valor do saque: ")
    while valor_saque <= 0:
        print("Valor do saque deve ser maior que zero!")
        valor_saque = obter_saldo("Valor do saque: ")

    if conta["saldo"] >= valor_saque:
        conta["saldo"] -= valor_saque
    elif conta["limite_credito"] >= valor_saque - conta["saldo"]:
        conta["saldo"] -= valor_saque
        print("Você está usando o seu limite de crédito!")
    else:
        print("Saldo insuficiente!")
        return

    conta["historico_operacoes"] += [("saque", -valor_saque)]
    print("Saque realizado com sucesso!")

# Função para consulta de saldo e de limite de crédito
def consultar_saldo():
    if not autenticar_conta():
        return

    print("Saldo em conta: R$", conta["saldo"])
    print("Limite de crédito: R$", conta["limite_credito"])

# Função para consulta de extrato/ histórico de operações na conta
def consultar_extrato():
    if not autenticar_conta():
        return

    print("Limite de crédito: R$", conta["limite_credito"])
    print("Últimas operações:")
    for operacao, valor in conta["historico_operacoes"]:
        if operacao == "depósito":
            print(f"Depósito: R${valor:.2f}")
        else:
            print(f"Saque: R${-valor:.2f}")
    print("Saldo em conta: R$", conta["saldo"])
    if conta["saldo"] < 0:
        print("Atenção ao seu saldo!")

# Função para cancelar a conta
def cancelar_conta():
    if not autenticar_conta():
        return

    confirmar = obter_entrada("Tem certeza que deseja cancelar a conta? (s/n) ")
    if confirmar == "s":
        conta["numero"] = None
        conta["nome"] = None
        conta["telefone"] = None
        conta["email"] = None
        conta["saldo"] = 0
        conta["limite_credito"] = 0
        conta["senha"] = None
        conta["historico_operacoes"] = []
        conta["bloqueado"] = False
        print("Conta cancelada com sucesso!")
    else:
        print("Operação cancelada.")

# Função principal que mostra o menu do banco
def main():
    opcoes = {
        1: cadastrar_conta,
        2: depositar,
        3: sacar,
        4: consultar_saldo,
        5: consultar_extrato,
        6: cancelar_conta
    }

    while True:
        print("MACK BANK – ESCOLHA UMA OPÇÃO")
        print("(1) CADASTRAR CONTA CORRENTE")
        print("(2) DEPOSITAR")
        print("(3) SACAR")
        print("(4) CONSULTAR SALDO")
        print("(5) CONSULTAR EXTRATO")
        print("(6) CANCELAR CONTA")
        print("(7) FINALIZAR")

        opcao = obter_entrada("Sua opção: ")
        if opcao.isdigit():  # verificar se é um número de 0 a 9
            opcao = int(opcao)
            if opcao == 7:
                print("MACK BANK – SOBRE")
                print("Este programa foi desenvolvido por: \n-> Pedro Henrique de Almeida Rodrigues :)")
                break
            elif opcao in opcoes:
                opcoes[opcao]()
            else:
                print("Opção inválida!")
main()
