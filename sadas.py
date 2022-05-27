from collections import Counter

candidatos = {
    '1': 'José da Silva',
    '2': 'Maria do Jurunas',
    '3': 'João do Tapanã'
}

def votar():
    votos = Counter()
    while True != 50:
        print("Lista de Candidatos\n")
        print(" O : Nulo\n 1 : Ana\n 2 : Pedro\n 3 : Rita\n 4 : Alfredp\n 5 : Regina\n 6 : Ricardo\n 10 : Branco\n")
        voto = input('Digite o número do candidato (ou "fim" para encerrar): ')
        if voto == 'fim':
            break # sai do while True
        if voto in candidatos: # se é um dos números de candidato válido
            votos.update([voto])
        else:
            print(f'Número inválido: {voto}')

    print('Resultado:')
    for numero, qtd_votos in votos.most_common():
        print(f'{candidatos[numero]} teve {qtd_votos} votos')

        turma = input('Digite sua turma :')
        if turma in turmas:
            turma.update([turma])
            print(f'turma  inválida: {voto}')