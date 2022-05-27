def porc(n):
    n = float((n / total) * 100)
    return n

votos = [0, 0, 0, 0, 0, 0, 0, 0]
validos = 0
invalidos = 0

print('-'*42)
print('VOTAÇÃO GRÊMIO ESTUDANTIL'.center(42))
print('-' * 42)

for i in range(0, 3):


    v = int(input('Digite o número do candidato que deseja votar: '))
    if v >= 1 and v <= 6:
        votos[v - 1] += 1
        validos+=1
    elif v == 10:
        votos[6] += 1
    elif v == 0:
        votos[7] += 1
    else:
        print('Número de candidato inválido, tente novamente!')

total = sum(votos)

print(f'\nForam computados {total} votos! Sendo {validos} válidos')

for i in range(6):
    print(f'Chapa {i + 1} : {votos[i]} votos ({round(porc(votos[i]), 2)}%)')

for i in range(5, 8):
    if i == 6:
        print(f"Brancos: {votos[6]} votos ({round(porc(votos[i]), 2)}%)")
    elif i == 7:
        print(f"Nulos: {votos[7]} votos ({round(porc(votos[i]), 2)}%)")