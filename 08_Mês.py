'''
Titulo: Mês por expenso
Autor; wagner korylo
Data: 01/10/2024

#Descricao: Faça um programa que receba o mês em 
#            e apresente-o por extenso. 
'''


#entrada de dados
mes = int(input('Inserir o numero do mes:')) # recebo o valordo usuário e converto para o valor enteiro 





#Processamento de dados
if mes == 1 : #   ex....se o usuario digitar o numero 1 entao o mes sera janeiro
    mes_extenso ='janeiro' # esse espaco do mes é a identação para ficar lincado ao mes 
elif mes == 2:
    mes_extenso = 'fevereiro'
elif mes ==3:
    mes_extenso = 'marco'
elif mes == 4 : 
    mes_extenso ='Abril'
elif mes == 5:
    mes_extenso = 'Maio'
elif mes ==6:
    mes_extenso = 'junho'
elif mes == 7 :
    mes_extenso ='julho'
elif mes == 8:
    mes_extenso = 'Agosto'
elif mes ==9:
    mes_extenso = 'Setembro'
elif mes == 10 : 
    mes_extenso ='outubro'
elif mes == 11:
    mes_extenso = 'Novembro'
elif mes ==12:
    mes_extenso = 'Dezembro'
else: 
     mes_extenso = 'mes nao existe'


#Saida de dados

print(mes_extenso)

# observação else + if = elif
 #else sempre na ultima linha para escrever a palavra qu nao existe
