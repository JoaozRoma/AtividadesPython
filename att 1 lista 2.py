def imposto():
    salario = float(input("Digite seu salário : "))
    if salario < 500:
        resultado = salario + 0.05

    elif salario >=500 and salario <=850:
        resultado = salario + 0.1

    elif salario > 850:
        resultado = salario + 0.15

    print("Resposta : ", resultado)


def Nsalario():
    salario = float(input("Digite seu salário : "))
    if salario > 1.500:
        resultado = salario + 25.00

    elif salario >= 750 and salario <= 1.500:
        resultado = salario + 50.00

    elif salario >= 450 and salario < 750:
        resultado = salario + 750.00

    elif salario <  450:
        resultado = salario + 100.00

    print("Novo Salario ; ",resultado)

def classf():
    salario = float(input("Digite seu salário : "))
    if salario <= 700.00:
        print("seu salario e mal remunerado")

    elif salario > 700.00:
        print("seu salario é bem remunarado")

menu = 1
while menu != 0:

    print(f"""
    1: Imposto
    2: Novo Salário 
    3: Classificação
    0: Sair""")


    menu= int(input('      Escolha sua opção : '))


    if menu == 1:
        imposto()

        menu2 = input('Deseja repetir o cadastro? s/n : ')
        if menu2 == 's':
            imposto()

    elif menu == 2:
        Nsalario()

        menu2 = input('Deseja repetir o cadastro? s/n : ')
        if menu2 == 's':
            Nsalario()

    elif menu == 3:
        classf()

        menu2 = input('Deseja repetir o cadastro? s/n : ')
        if menu2 == 's':
            classf()

    else:
        print('VALEU TMJ!')


