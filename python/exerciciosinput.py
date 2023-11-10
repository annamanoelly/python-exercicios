'''Exercício1'''
n1_c=int(input('Digite o primeiro número \n>'))
n2_c=int(input('Digite o segundo número \n>'))
op=(n1_c+n2_c)
print('A soma dos números é:',op,"\n")
op=(n1_c-n2_c)
print('A subtração dos números é:',op,'\n')
op=(n1_c* n2_c)
print('A multiplicação dos números é:',op,'\n')
op=(n1_c//n2_c)
print('O valor da divisão inteira é:',op,'\n')
op=(n1_c/n2_c)
print('O valor da divisão decimal é:',op,'\n')
op=(n1_c** n2_c)
print('O valor da potência é:',op,'\n')
print()

'''Exercício2'''
peso_f=float(input('Digite seu peso \n>'))
print(peso_f)
altura=input('Digite sua altura \n>')
altura_f=float(altura)
print('O IMC é:',peso_f/altura_f**2)
print()

'''Exercício3'''
idd=input('Sua idade em números: \n>')
idade=int(idd)
meses=idade*12
dias=idade*365
print('Você já viveu',idade*12,'meses e',meses*365,'dias')

'''Execicio 1'''
peso=input("Digite seu peso \n>")
peso_f=float(peso)
print(peso_f)
altura=input("Digite seu altura \n>")
altura_f=float(altura)
print(altura_f)
print("O IMC é",peso_f/altura_f**altura_f)
print()

'''Exercicio 2'''
n1=input('Digite o primeiro número \n>')
n2=input('Digite o segundo número \n>')
n1_c=int(n1)
n2_c=int(n2)
n1_f=float(n1)
n2_f=float(n2)
print('A soma dos dois números é: \n>',n1_c+n2_c)
print('A subtração dos dois números é \n>',n1_c-n2_c)
print('A múltiplicação dos dois números é \n>',n1_c*n2_c)
print('O valor da potência inteira é: \n>',n1_c**n2_c)
print('O valor da potência em decimal é: \n> ',n1_f**n2_f)
print('O valor da divisão inteira é: \n>',n1_c//n2_c)
print('O valor do resto é: \n>',n1_c%n2_c)

