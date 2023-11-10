'''Programa para pegar um numero e multiplicar por ele mesmo,conversão em inteiro e decimal'''
Idade=input("Digite a sua idade \n>")
Idade_c=int(Idade)
res=Idade_c*Idade_c
print(res)
res_f=float(res)
print(res_f)
print("A idade é",Idade_c,"e ela multiplicada por ela mesma é",res)
# Erroooo,não pode concatenar texto com inteiro (var="A idade é" +Idade_c+"e ela mumultiplicada é"+res)
#str contração de string

final="A idade é"+str(Idade_c),"e ela multiplicada pr ela mesma é"+str(res)
print(final)
print()
#Descobrir a variavel
#loka=???
#t=type(loka)
#print(t)
print()

lk=10
print(type(lk))
lk=10.50
print(type(lk))
lk="10.50"
print(type(lk))
lk=False
print(type(lk)) 
print()
#num1=int(num1)
#num2=int(num2)'''
#conversão dele mesmo



'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade 
de números impares.'''

qtdPares = 0
qtdImpares=0
for i in range(0,10):
  num1=int(input("Digite o " + str(i+1) + " número:"))
  if (num1 % 2)== 0:
      qtdPares = (qtdPares + 1)
  if (num1%2)==1:
    #print("O numero é par")
    qtdImpares=(qtdImpares +1)
print("A quantidade de números pares é: ", qtdPares)
print("A quantidade de números impares é:",qtdImpares)
print()
'''Concatenação de Strings'''
nome = 'Anna'
sobrenome = 'Batani'

nome_completo = nome + ' ' + sobrenome

print(nome_completo) # Anna Batani

