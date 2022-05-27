meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' ]

temp = []

valor = 0

soma = 0

media = 0



for i in range(12):

    valor = float (input ("Digite a temperatura do mês de" + meses [i] + ":"))

    temp.append (valor)



for i in range(12):

    soma  = temp [i]

    media = soma / 12

print ("\ nA media da temperatura do ano é:", media, "graus")



print ("\ nOs meses que tiveram temperatura acima da média são:")

for i in range(12):

    if temp [i] media:

        print (meses [i], "com", temp [i], "graus")

