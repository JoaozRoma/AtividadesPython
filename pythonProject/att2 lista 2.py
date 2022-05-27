def clear():
    print("\n" * 40)


while True:
    print("---------- LOJA TABAJARA -----------")
    n = 1
    total = 0

    while True:
        preco = float(input("Produto {}: R$ ".format(n)))
        n += 1
        total += preco
        if preco == 0:
            break

    print("------------------------------------")

    print("Total: R$ {:.2f} ".format(total))
    dinheiro = float(input("Dinheiro: R$ "))
    print("Troco: R$ {:.2f}".format(dinheiro - total))

    print("------------------------------------")

    reset = input("pressione 0 para reset, 1 para encerrar: ")
    if reset == "0":
        clear()
        continue
    else:
        clear()
        print("Encerrando caixa...")
        break