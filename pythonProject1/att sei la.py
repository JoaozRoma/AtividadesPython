
class ContaCorrente:

    def __init__(self, numero_conta, nome , saldo=0) :
        self . saldo = saldo
        self . numero_conta = numero_conta
        self . nome = nome

    def alterar_nome(self, nome) :
        self . nome = nome
        return self.nome

    def getNome(self):
        return self.nome

    def deposito(self, v_deposito) :
        self . saldo += v_deposito
        return self.saldo

    def saque(self, v_saque) :
        self . saldo -= v_saque
        return self.saldo

resultado = ContaCorrente(19,"joão roma")

print("Bem vindo: ")
opc = int(input("Digite a opção desejada (Saque = 1, Depósito = 2, alterar nome = 3): "))
if opc == 1 :


    saque = float(input("Insira o valor do saque: "))
    resultado.saque(saque)
    print("Saldo atual: ", resultado.saldo)

elif opc == 2 :


    deposito  = float(input("Insira o valor à ser depositado: "))
    resultado.deposito(deposito)
    print("Saldo atual: ", resultado.saldo)

elif opc == 3 :

    novo = input("Insira o novo nome: ")
    resultado.alterar_nome(novo)

#
print("===============================")
print("Número da conta: ", resultado.numero_conta, "\nNome do correntista: ", resultado.getNome(), "\nSaldo: ", resultado.saldo)
print("===============================")

