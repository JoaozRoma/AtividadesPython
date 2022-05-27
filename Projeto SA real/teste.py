 # op = 1
# while op !=0:
#     print(f"""
#       ### B.W Sistema de Filmes ###
#       1 - Ranking de Filmes
#       2 - CRUD
#       3 - Sugestão de filme randômica
#       4 - Pesquisa por gênero
#       0 - Sair do Programa
#       """)
#     op = int(input('Escolha sua opção : '))
#
#     if op ==1:
#         Ranking()
#     elif op == 2:
#         x = 1
#         while x !=0:
#             print(f"""
#                   ### B.W Sistema de Filmes (CRUD) ###
#                   1 - Adicionar Filmes
#                   2 - Deletar um Filme
#                   3 - Exibir Filmes nos registros
#                   4 - Atualizar um filme no registro
#                   0 - Sair da tela
#                   """)
#             x = int(input("Escolha sua opção : "))
#             if x ==1:
#                 Insert()
#             elif x ==2:
#                 Delete()
#             elif x==3:
#                 Consultar()
#             elif x==4:
#                 t1 = input("Insira o ID do filme para um Update : ")
#                 if VerificaId() == 'nao':
#                     continue
#                 ConsultaEspecial(t1)
#                 print("\nInsira os novos registro do filme : ")
#                 titulof = input("Título novo : ")
#                 generof = input("Gênero novo : ")
#                 anof = input("Ano de Lançamento : ")
#                 diretorf = input("Diretor : ")
#                 notaf = input("Nota : ")
#
#                 declaracao = """UPDATE filmes SET titulo = """ '\'' + titulof + '\','"""
#                 genero = """ '\'' + generof + '\','""" ano = """'\'' + anof + '\','""" diretor = """'\'' + diretorf + '\','"""
#                 nota =  """'' + notaf + ' WHERE id_filme = ' + t1
#                 Update(declaracao)
#
#             elif x ==0:
#                 print("Saindo da tela.")
#             else:
#                 print("Opção inválida, tente novamente.")
#     elif op == 3:
#         Random()
#     elif op ==4:
#         print("Insira o gênero : ")
#         id = input("Gênero : ")
#         declaracao1 = """SELECT * from filmes WHERE genero = """ '\'' + id + '\';'
#         ConsultaGen(declaracao1)
#     elif op == 5:
#         VerificaId()
#     elif op ==0:
#         print("Fechando o Sistema.")
#     else:
#         print("Opção inválida, tente novamente.")