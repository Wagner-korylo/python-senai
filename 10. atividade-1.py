'''
Titulo: ctegoria PELA idade
Autor; wagner korylo
Data: 01/10/2024

#Descrição: Faça um programa para exibir a ocupação de um funcionário a partir de seu código de
profissão, de acordo com a tabela abaixo;

#Código de Profissão Ocupação
1 Matemático
2 Analista de Sistemas
3 Físico
4 Arquiteto
5 Piloto de Aeronaves
'''


# Dados de entrada
profissão= int(input('digite o código da profissão:'))

# preessamento de dados
if   profissão == 1:
     profissão = 'Matemático'
elif profissão == 2:
     profissão = 'analista de sistemas'
elif profissão == 3:
     profissão = 'Fisico'
elif profissão == 4:
     profissão = 'Arquiteto'
elif profissão == 5:
     profissão = 'Piloto de aeronaves'

# Dados de saida
print(profissão)