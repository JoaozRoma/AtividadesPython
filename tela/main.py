from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha  '), sg.InputText(key='senha', size=(20, 1), password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# janela
janela = sg.Window('Tela de Login',layout)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos =='Entrar':

        if valores['usuario']=='Klaus' and valores['senha'] =='1':
            print('Bem vindo !' )

        else:
            print ('Credenciais inválidas, verifique!')



