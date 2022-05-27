from collections import Counter

candidatos = \
{
'0' : 'Nulo',
'1' : 'Ana',
'2' : 'Pedro',
'3' : 'Rita',
'4' : 'Alfredo',
'5' : 'Regina',
'6' : 'Ricardo',
'10': 'Branco'
}

turmas = \
{
 '1' : 'Turma 1',
 '2' : 'Turma 2',
 '3' : 'Turma 3'
}

def votar():
 votos = Counter()
 SelecTurma = Counter()
 for i in range(2):
   print("Lista de Candidatos\n")
   print(" O : Nulo\n 1 : Ana\n 2 : Pedro\n 3 : Rita\n 4 : Alfredp\n 5 : Regina\n 6 : Ricardo\n 10 : Branco\n")
   voto = input('Digite o número do candidato: ')
   if voto in candidatos:
    votos.update([voto])
   else:
    print(f'Número inválido: {voto}')

   print("Lista de Turma\n")
   print("\n 1 : Turma 1\n 2 : Turma 2\n 3 : Turma 3")

   VotoTurma = input("Digite o número da sua turma : ")
   if VotoTurma in turmas:
    SelecTurma.update([VotoTurma])
   else:
    print(f'Número inválido: {VotoTurma}')


   print('Resultado:')
   for numero, qtd_votos in votos.most_common():
      print(f'{candidatos[numero]} teve {qtd_votos} votos')
      print("============================================")

   print('Resultado:')
   for numero, qtd_SelecTurma in SelecTurma.most_common():
       print(f'{turmas[numero]} votou {qtd_SelecTurma} vezes')
       print("==============================================")

votar()