
year = 0

while True:

    popA = int(input("Digite o número da população 'A' "))
    txA = float(input("Digite a taxa de crescimento da população 'A' em '%' "))
    popB = int(input("Digite o número da população 'B' "))
    txB = float(input("Digite a taxa de crescimento da população 'B' em '%' "))
    percentA = txA / 100
    percentB = txB / 100

    if popA <= 0:
        print("Valor da população 'A' inválido.")
    elif popB <= 0:
        print("Valor da população 'B' inválido.")
    else:
        break

while popA <= popB:

            popA += popA * percentA
            popB += popB * percentB
            year += 1
print("A população 'A' se iguala ou ultrapassa a população 'B' em", year,"anos.")
