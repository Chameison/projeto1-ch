#Este programa emite um relátorio final ao término do ano letivo de todas as turmas!
import os

print ("\t\t\t\tBem-Vindo(a)! \n\tEste programa imprime um relatório de notas de uma turma!")

nota = 0
media = 0
soma = 0
acima = 0
namedia = 0
abaixo = 0
maior = 0
menor = 100
turma = 0
n = 0
i = 1
op = 0
es = 1

while(es ==1):
    turma = str(input("\n\nDigite o nome da turma: "))
    n = int (input("\n\nDigite a quantidade de alunos da turma: "))
    while (i <= n):
        nota = float(input("\nDigite nota: "))
        soma = soma + nota
        if (nota > maior):
            maior = nota
        if (nota < menor):
            menor = nota
        if (nota < 70):
            abaixo = abaixo + 1
        elif (nota == 70):
            namedia = namedia + 1
        elif (nota > 70):
            acima = acima + 1
        i = i + 1


    media = soma/n
    print ("\n\nO relátorio da turma ", turma,"é: ")
    print ("\nA quantidade de notas lidas foi: ", n)
    print ("\nO somatório total das notas foi: ", soma)
    print ("\nA média das notas foi: ", media)
    print ("\nA maior nota foi: ", maior)
    print ("\nA menor nota foi: ", menor)
    print ("\nA quantidade de notas superiores á média foi: ", acima)
    print ("\nA quantidade de notas em cima da média foi: ", namedia)
    print ("\nA quantidade de notas inferiores á média foi: ", abaixo)
    print ("\n\n\nDeseja realizar outro relátorio de notas?")
    op = int(input("\nDigite 1 para SIM \nDigite 2 para NÃO \n\nEscolha: "))
    if (op == 1):
        es = 1
    else:
        es = 2
print ("\n\n\n\t\tEste é um programa da equipe: Guardiões da Galáxia!")
print ("\n\t\t\tObrigada por utilizar nosso programa!")

os.system ("pause")
