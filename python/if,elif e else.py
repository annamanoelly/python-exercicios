'''Algoritimo para verificar o comando if'''
x=int(input('Digite um número \n>'))
if(x>20):
  print('x é maior que 20')    
print('até mais')
print()

'''outro exemplo'''
dado=input('Digite um número \n')
num=int(dado)
if(num>20):
    print('O número é maior que 20 \n')
    print()
    
#se=if
#se=if
#se for falso e pertencer ao if não vai executar o print
#exemplo:if(num >=20): maior e igual a 20
#if(num==20):igual a 
#if(num!=20): diferente de
#if(num<20): menor que
#identação=escrever conforme as regras do programa
print()

'''Exercício1'''
a=int(input('Digite um número \n'))
b=int(input('digite outro número \n'))
if(a>b):
   print('a é maior que b \n')
if(a<b):
    print('a é menor que b \n')
if(a==b):
    print('a é igual a b \n')
if(a!=b):
    print('a é diferente de b \n')
print('ok,obrigado!')
print() 

'''Verifique se é par ou ímpar'''
a=int(input('Digite um número \n>'))
if((a%2==0)):
    print('par')
else:
    print('ímpar')
print()

'''Verificar se os três números são maiores ou menores entre si'''
n1=int(input('Digite um número \n>'))
n2=int(input('Digite o segundo número \n>'))
n3=int(input('Digite o terceiro número \n>'))
if n1>n2:
   if n1>n3:
       print('n1 é maior')
if n2>n1:
    if n2>n3:
       print('n2 é maior que n3')
if n3>n1:
    if n3>n2:
       print('n3 é o maior')

#usando o else
if(n1>n2)and(n2>n3):
    print('n1')
else:
    if(n2>n3)and(n2>n1):
            print(n2)
    else:
        if(n3>n1)and(n3>n2):
            print(n3)
print()

'''digite um número de 1 a 7 e mostre o dia da semana de acordo com o número'''
n1=int(input('Digite um número de um 1 a 7 \n>'))
if n1==1:
    print('segunda-feira')
elif n1==2:
         print('terça-feira')
elif n1==3:
    print('quarta-feira')
elif n1==4:
    print('quinta-feira')
elif n1==5:
    print('sexta-feira')
elif n1==6:
    print('sábado')
elif n1==7:
    print('domingo')
else:
    print('opção inválido')
#sem converter pra inteiro poderia só colocar:if dia=="1":
#elif usa quando tem multtiplas comparações
