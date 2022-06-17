#Este programa determina o IMC(Índice de Massa Corporal)!
import os

print ("\n\t\t\t\tBem-Vindo(a)! \n\tEste programa calcula o IMC (Índice de Massa Corporal)!")

peso = 0
altura = 0
IMC = 0
op = 1

while (op == 1):
    peso = float(input("\n\nDigite o seu peso em kg: "))
    altura = float(input("\n\nDigite a sua altura: "))
    IMC = peso/(altura* altura)
    print ("\n\nSeu IMC é: ", IMC)
    if (IMC <= 16):
        print ("\nVocê se encontra em Magreza Grave! Procure um médico com urgência!")
    elif (16 < IMC <= 17):
        print ("\nVocê se encontra em Magreza Moderada! Procure um médico assim que possível!")
    elif (17 < IMC <= 18.5):
        print ("\nVocê se encontra em Magreza Leve! Cuide de sua alimentação!")
    elif (18.5 < IMC <= 25):
        print ("\nParabéns! Seu IMC está classificado como Saudável! Você está cuidando de sua saúde!")
    elif (25 < IMC <= 30):
        print ("\nVocê se encontra em Sobrepeso! Cuidado! Precisa controlar sua alimentação e realiza atividades físicas!")
    elif (30 < IMC < 35):
        print ("\nVocê se encontra em Obesidade Grau I! Cuidado! Procure um médico assim que possível! Cuide de sua alimentação!")
    elif (35 < IMC <= 40):
        print ("\nVocê se encontra em Obesidade Grau II(severa)! Cuidado! Procure um médico o mais rápido possível! Precisa de dieta e atividades físicas!")
    elif (IMC >= 45):
        print ("\nVocê se encontra em Obesidade Grau III(mórbida)! Precisa procurar um médico com a máxima urgência!")
    print ("\n\n\nDeseja calcular o IMC, novamente?")
    op = int(input("\n\nDigite 1 para SIM \nE digite 2 para NÃO \n\nEscolha: "))
    if (op == 1):
           op == 1
    else:
        op == 2
print ("\n\n\n\tEste é um programa da equipe: Guardiões da Galáxia!")
print ("\n\t\tObrigada por utilizar nosso programa!")
os.system ("pause")
