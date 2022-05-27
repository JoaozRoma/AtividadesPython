import mysql.connector
from mysql.connector import Error

def Conexao():
    try:
        global conn
        conn = mysql.connector.connect(host='localhost',database='projetosa',user='root',password='')
    except Error as e:
        print("Erro de conexão",e)


def Consultar():
    try:
        Conexao()
        consulta_bdd =("SELECT * from filmes")
        cursor = conn.cursor()
        cursor.execute(consulta_bdd)
        linhas = cursor.fetchall()
        print("Total de filmes no Sistema : ",cursor.rowcount)

        print("\nMostrando todos os filmes cadastrados ")
        for linha in linhas:
            print("ID do Filme :",linha[0])
            print("Título :",linha[1])
            print("Gênero :",linha[2])
            print("Ano de Lançamento :",linha[3])
            print("Diretor do Filme :",linha[4])
            print("Nota :",linha[5],"\n")

    except Error as e:
        print("Falha a exibir os filmes na BDD : ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            cursor.close()
            print("Conexão Encerrada!")


def Insert():
    print("Cadastro de Filme no BDD")
    print("Insira os dados conforme solicitados.")
    t1 = input("ID do Filme : ")
    t2 = input("Título : ")
    t3 = input("Gênero : ")
    t4 = input("Ano de Lançamento : ")
    t5 = input("Diretor do Filme : ")
    t6 = input("Nota : ")
    dados = t1 + ',\'' + t2 + '\',\'' + t3 + '\',\'' + t4 + '\',\'' + t5 + '\',' + t6 + ')'
    insert_bdd = """INSERT INTO filmes
            (id_filme,titulo,genero,ano,diretor,nota) 
            VALUES ("""
    sql = insert_bdd + dados
    try:
        Conexao()
        enviar = sql
        cursor = conn.cursor()
        cursor.execute(enviar)
        conn.commit()
        print(cursor.rowcount,"Registros adicionados na BDD.")
        cursor.close()
    except Error as e:
        print("Falha aou inserir um registro na BDD : ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            print("Conexão Encerrada!")




op = 1
while op !=0:
    print(f"""
      ### B.W Sistema de Filmes ###
      1 - Consulta de Filmes
      2 - Insert na base 
      0 - Sair do Programa
      """)
    op = int(input('Escolha sua opção:'))

    if op ==1:
        Consultar()
    elif op ==2:
        Insert()
    elif op ==0:
        print("Fechando o Sistema.")
    else:
        print("Opção inválida, tente novamente.")

conn.close()