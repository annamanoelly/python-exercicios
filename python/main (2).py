'''Faça um programa que peça dois números decimais ao usuário 
e imprima a soma desses dois números, a multiplicação, a subtração e a média.'''
n1=float(input('Digite o primeiro número \n>'))
n2=float(input('Digite o segundo número \n>'))
print('A soma dos números é :',n1+n2)
print('A multiplicação dos números é:',n1*n2)
print('A subtração dos números é:',n1-n2)
print('A média dos númros é:',(n1+n2)/2)
print()

'''2 - Escreva um programa que peça ao usuário um valor em metros e o exiba convertido em centímetros.'''
metros=float(input('Digite um número \n>'))
centímetros=metros*100
print('Em centímetros:',centímetros)
print()

'''3 - Faça um programa que solicite ao usuário digitar a altura e largura de uma determinada área a ser medida. 
Imprima na tela do valor área total conforme os valores digitados pelo usuário.'''

altura=int(input('Digite a altura \n>'))
largura=int(input('Digite a largura \n>'))
print('A área total é:',altura+largura)
print()

'''4 - Faça um programa que solicite ao usuário sua idade. 
Depois Imprima esta idade na tela e informe o ano de nascimento do usuário que digitou a idade.'''
idade=int(input('Digite sua idade \n>'))
ano=2022-idade
print('Sua idade:',idade,'anos e você nasceu em:',ano)
print()

'''5 - Escreva um programa que peça ao usuário a quantidade de dias, horas, minutos e segundos.
Calcule o total em segundos.'''
dias = int(input('Dias:'))
horas = int(input('Horas:'))
minutos = int(input('Minutos:'))
segundos = int(input('Segundos:'))
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print('Total em segundos:', total_em_segundos)
print()

'''6 - Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço apagar.'''
preço=float(input('Digite o preço da mercadoria \n>'))
desconto=float(input('Digite o percentual de desconto \n>'))
valor_do_desconto=preço*desconto/100
pagar=preço-valor_do_desconto
print('preço:',preço,',valor de desconto:',desconto)
print('percentual de desconto:',valor_do_desconto)
print('total a pagar:',pagar)

'''7 - Calcule o tempo de uma viagem de carro. 
Pergunte ao usuário distância a percorrer e a velocidade média esperada para a viagem.'''
distância=float(input('Digite a distância \n>'))
velocidade_média=float(input('Digite a velocidade média \n>'))
tempo=int(distância/velocidade_média)
print('Tempo de viagem estimado é de:',tempo,'hora')
print()

'''8 - Converta uma temperatura digitada pelo usuário de Celsius para Fahrenheit. F = (9*C)/5 + 32.'''
c=float(input('Digite a temperatura em Celsius \n>'))
f=((9*c/5)+32)
print('A temperatura em Fahrenheit é:',f)
print()

'''9 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.'''
km=float(input('Digite a quantidade em km \n>'))
dias=int(input('Digite a quantidades de dias \n>'))
custo_por_dia=60
custo_por_km=0.15
r=km*custo_por_km+dias*custo_por_dia
print('Total a pagar:',r)
print()

'''10 - Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidadede cigarros fumados por dia e quantos anos ele já fumou. 
Considerando que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. 
Exiba o total de dias.'''
cigarros_por_dia=int(input('Cigarros por dia \n>'))
anos_fumando=int(input('Anos fumando \n>'))
redução_em_minutos=anos_fumando*365*cigarros_por_dia*10
redução_em_dias=(redução_em_minutos//(24*60))
print('Reducão de vida:',redução_em_dias,'dias')
print()

'''11 - Faça um programa que solicite que o usuário digite um número qualquer e armazena na variavel "var". 
Imprima na tela o tipo de variável "var". Depois converta para inteiro e imprima novamente o tipo de variável. 
Depois converta para float e imprima novamente o tipo de variável. 
Atribua para var o valor "False" e imprima novamente o tipo de variável'''
var=input('Digite um número \n>')
print(type(var))
var=int(var)
print(type(var))
var=float(var)
print(type(var))
var=False
print(type(var))

'''quanto dinheiro vc tem na carteira e mostre quantos dolares ela pode comprar'''
real=float(input('Quantos vc tem na carteira'))
dolar=real / 5.23
print('Com {} voce pode comprar US${}' .format(real,dolar))

'''1 - Faça um programa onde o usuário deverá digitar dois números. 
Verifique qual dos dois números é maior e imprima na tela informando qual é o maior.'''
n1=int(input('Primeiro número \n>'))
n2=int(input('Segundo número \n>'))
if n1>n2:
    print('O primeiro número é maior!')
if n2>n1:
    print('O segundo número é maior!')
print()

'''2 - Faça um programa onde o usuário deverá digitar um número. 
Depois informe se o número digitado é par ou impar.'''
n=int(input('Digite um número \n>'))
if((n%2==0)):
    print('par')
else:
    print('ímpar')
print()

'''3 - Escreva um programa que deverá perguntar três números ao usuário. 
Imprima estes números em ordem crescente (do menor para o maior)'''
n1=int(input('Primeiro número \n>'))
n2=int(input('Segundo número \n>'))
n2=int(input('Terceiro número \n>'))


'''4 - Solicite ao usuário que digite um número. 
Imprima todos os números de 0 até o número digitado pelo usuário.'''
i=int(input('Digite um número \n> '))
x=0
for i in range(i):
    if (x<=i):
       print(i)
    x=x+1
    
'''5 - Faça um algoritmo onde o usuário deverá digitar um número. 
O programa deverá listar todos os números pares até o número digitado pelo usuário.'''
i=int(input('Digite um número \n>'))
for i in range(i):
    if (i%2)==0:
       print(i,'par')
 
'''6 - Faça um algoritmo que liste todos os números ímpares até 1000. 
Utilize um laço de repetição que faça incrementos de 3 em 3.'''
for i in range (0,1001):
    if (i%3==0):
        print(i,'ímpar')
#incompleto 

'''7 - Faça um programa que solicite dois números ao usuário. Utiliza uma multiplicação por somatória.
Ex:o usuário digita 3 e 4. logo, deverá somar 4+4+4.'''
n1=int(input('Primeiro número \n>'))
n2=int(input('Segundo número \n>'))
for i in range(n1+n2):
    if (n1*n2):
        print(n1+n2)












 














