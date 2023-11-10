'''1. Faça um algoritmo que:
a) leia o valor para a variável HT (horas trabalhadas no mês);
b) leia o valor para a variável VH (valor hora trabalhada):
c) leia o valor para a variável PD (percentual de desconto);
d) Calcule o salário bruto => SB = HT * VH;
e) Calcule o total de desconto => TD = (PD/100)*SB;
f) Calcule o salário líquido => SL = SB – TD;
g) Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário Liquido.'''
ht=int(input("Digite a quantidade de horas trabalhadas no mês \n>"))
vh=float(input("Digite o valor da hora trabalhada \n>"))
pd=int(input("Digite o valor de percentual de desconto \n>"))
sb=ht*vh
td=(pd/100)*sb
sl=sb-td
print("horas trabalhadas:",ht, ";valor da hora trabalhada:",vh, ";salário bruto:",sb, ";desconto:",td, ";e o salário liquido:",sl,".")

'''2) Crie um algoritmo onde o usuário deverá digitar um numeral de 1 a 5 para exibir mensagens, e caso digite 0,
o programa deverá encerrar. Se o usuário digitar algo fora deste escopo, o programa deverá retornar uma
mensagem que foi digitada uma opção incorreta. Para cada número digitado, o programa deverá mostrar o
seguinte:
Número 1: Definição de compilador e interpretador.
Número 2: Cite 5 tipos de dados e o que representa cada um. (Ex: boolean = assume somente dois valores:
true ou false).
Número 3: Definição de typecast e indentação.
Número 4: Definição de Linguagens de Programação com tipagem forte e fraca.
Número 5: Definição de variável e constante. Além disso, informe o que é preciso para declarar uma variável
ou uma constante.
Você deverá escrever o que significa cada um destes itens com suas próprias palavras.'''

num=int(input("Digite um número \n>"))
while num !=0:
 if num == 1:
  print(" Um interpretador lê um programa de alto nível (chamado de código fonte) e executa ele, ou seja, realiza as ações do programa passo a passo e um compilador lê o programa de alto nível e traduz ele completamente antes de executá-lo.")
 elif num == 2:
  print("int= mostra um número inteiro / float= coloca um número em decimal / type = mostra o tipo da variavel / boolean = assume somente dois valores que são true ou fals / str = strings que nada mais são do que sequências (cadeias) de caracteres")
 elif num == 3:
   print("typecast=descobre o tipo de variavel que o programa está usando / identação= é o recuo do texto em relação a sua margem, é essencial para o bom funcionamento do código.")
 elif num == 4:
   print("Linguagem de programação: conjunto de símbolos e códigos usados para dar instruções ao computador / tipagem forte: a linguagem exige que o tipo de dado de um valor seja do mesmo tipo de variável ao qual este valor será atribuído. tipagem fraca: Quando é fraco, não há necessidade de explicitar o tipo de dado, e ele pode mudar conforme o valor que é atribuído a variável.")
 elif num == 5:
   print("A definição de uma variável é que o  valor dela tá sempre mudando e a definição de constante é que o valor permanece sempre o mesmo. / Para declarar uma variável ou uma constante precisamos informar de que tipo a mesma é. ")
 else:
   print("Opção inválida")
 num=int(input("Digite um número ou Zero para encerrar \n>"))



'''3) Elabore um algoritmo que solicite ao usuário um número de 1 a 12. Para cada número, o programa deverá
exibir por extenso o mês correspondente. (ex: Se o usuário digitar 2, deverá escrever “Fevereiro”). Ao digitar
zero, o programa deverá encerrar. Se o usuário digitar algo fora deste escopo, o programa deverá retornar uma
mensagem que foi digitada uma opção incorreta.'''

num=int(input("Digite um número de 1 até 12 \n>"))
while num!=0:
 if num==1:
   print("Janeiro")
 elif num==2:
   print("Fevereiro")
 elif num==3:
   print("Março")
 elif num==4:
   print("Abril")
 elif num==5:
   print("Maio")
 elif num==6:
   print("Junho")
 elif num==7:
   print("Julho")
 elif num==8:
     print("Agosto")
 elif num==9:
    print("Setembro")
 elif num==10:
    print("Outubro")
 elif num==11:
   print("Novembro")
 elif num==12:
  print("Dezembro")
 elif num==12:
  print("Dezembro")
 else:
  print("Opção inválida")
 num=int(input("Digite um número de 1 até 12 ou Zero para encerrar \n>"))



'''4) Construa um algoritmo onde o usuário informará numericamente o dia, o mês e o ano de uma determinada
data e o programa informará se aquela é uma data válida. Considere que os meses 1,3,5,7,8,10 e 12 poderão
ter no máximo 31 dias; os meses 4, 6, 9 e 11 poderão ter no máximo 30 dias e o mês 2 tem no máximo 28 dias.
Se a data estiver correta, imprimir no formato dd/mm/AAAA. Se a data for inválida, imprima na tela “Data
Inválida.'''
while 1==1:
    d=int(input("Digite o dia \n>"))
    m=int(input("Digite o mês \n>"))
    a=int(input("Digite o ano \n>"))
    if (d >=32 ):
        print("dia inválido")
        break
    elif (m >=13):
        print("mês inválido")
        break
    elif (d > 28 and m == 2):
        print("data inválida")
        break
    elif(d <= 30 and m == 4,6,9,11 ):
        print("data válida",d,"/",m,"/",a,)
        break
    elif(d <= 31 and m == 1,3,5,7,8,10,12):
        print("data válida",d,"/",m,"/",a,)
    else:
        print("data inválida")
    





'''5) Faça um algoritmo que solicite 10 números ao usuário. Ao final, o programa deverá exibir na tela:
a) O maior valor digitado
b) O menor valor digitado
c) O somatório dos valores digitados
d) Média dos valores digitados'''

num=int(input("Digite o 1 número \n>"))
maior_valor=num
menor_valor=num
soma = 0
media=0
for i in range (1,11):
    num = int(input("Digite mais um número:\n> "))
    if (i==1):
        maior_valor=num
    if (num < menor_valor):
        menor_valor=num
    soma=soma+num
print("maior valor:",maior_valor)
print("menor_valor:",menor_valor)
print("A soma dos valores é",soma)
print("A média dos valores é",(soma/10))


















