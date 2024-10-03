'''

  Faça um programa Autor; wagner korylo
Data: 26/09/2024
Descricao:que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que:
Salário < R$ 1000,00 aumento de 25%.
Salário >= R$ 1000,00 e <; R$ 2000,00 aumento de 15%.
Salário >= R$ 2000,00 aumento de 10%.




#comentario em linha ctrl + ;
# ctrl + shift + alt + (cima/baixo/direita/esquerda)
# serve paracelecionar e escrever (varias colunas juntas)

'''

# Dados de entrada

salario = float (input('Digite o salario:'))



#Processamento de dados:
if salario < 1000:
    salario_reajuste = salario * 1.25
if salario >= 1000 and salario < 2000:
    reajuste = salario * 0.15
    salario_reajuste = salario + reajuste
if salario >= 2000:
    salario_reajuste = salario * 1.1


#Saida de dados:
 
print ('Seu novo salario:', salario_reajuste)






