'''digite um número e veja em qual faixa etária '''
n=int(input('Digite um número \n>'))
if n>=0 and n<10:
    print('criança')
elif n>=11 and n<=17:
    print('adolescente')
elif n>=18 and n<=25:
    print('jovem')
elif n>=26 and n<=50:
    print('adulto')
elif n>=51 and n<=60:
    print('experiente')
elif n>=61 and n<=120:
    print('3º idade')
else:
    print('Número inválido')
#Duas comparações lógicas,tem que ser true
#se a idade for menor ou maior "or"
#if(num>0)and (num%2==1)and'''

'''Digite três medidas e imprima qual é o tipo de triangulo de acordo com a medida'''
t1=float(input('Digite a primeira medida \n>'))
t2=float(input('Digite a segunda medida \n>'))
t3=float(input('Digite a terceira medida \n>'))
#if t1<=0 or b<=0 or t3<=0:
#print('Lados nulos ou negativos não são aceitos')
if t1==t2 and t2==t3:
    print('Triangulo equilátero')
    #tres lados iguais
elif t1!=t2 and t2!=t3 and t3!=t1:
    print('Triangulo escaleno')
    #tres lados diferentes
elif t1==t2 or t2==t3 or t3==t1:
    print('Triangulo isósceles')
    #dois lados iguais
else:
    ('Algo de errado não está certo')
print()
        
op=input(digite de 1 a 3 \n')
if (op=="1"):
   print('Bom dia')
elif (op=="2"):
    print('Boa tarde')
elif(op=="3"):
    print('Boa noite')
else:
    print('opção invalida')




   









