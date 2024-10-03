'''''
Titulo: ctegoria PELA idade
Autor; wagner korylo
Data: 01/10/2024

#descrição:Escreva um programa que leia 
# a idade de um indivíduo e escreva a faixa etária a que
pertence, de acordo com a tabela abaixo;

Faixa etária Classificação
<=12 Criança
13~17 Adolescente
18^59 Adulto
> 60 Especialista
'''



#Entrada de dados
idade = int(input('digite a idade do usuário:'))  # CRIOU A VARIAVEL CHAMADA IDADE: SE NAO TEM PONTO FLUTUANTE (EX) PONTO, ENTAO E UM PONTO INTEIRO (INT)
categoria = 'sem categoria'

#Processamento de dados
if  idade <= 12: 
    categoria = 'Criança'
elif idade >= 13 and idade <= 17: 
    categoria:'Adolescente'
elif idade >= 18 and idade <=59: 
    categoria: 'adulto'
elif idade >= 60: 
    categoria:'Especialista'

#Saida de dados
print('categoria usuário:', categoria)


# and operação logica:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   