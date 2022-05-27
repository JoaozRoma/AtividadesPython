print('='*50)
print(f'{msg:=^50}')
print('='*50)
msg='PANIFICADORA PÃO DE ONTEM - TABELA DE PREÇOS'
valor= float(input('PREÇO DO PÃO: R$ '))
for n in range(1,51):
print(f'{n:>2} - R$ {n*valor:.2f}')