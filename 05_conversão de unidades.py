
''
#Titulo: conversão de unidades
#Autor: Wagner Korylo
#Data: 19/0/09/2024
#Descrição: Faça um programa que redebe um numero em pés, faça as converções
#           a seguir e mostre os resultados.
#           --------------------------------------------
#            - Polegadas;
#            - Jardas;
#            - Milhas;
# sabe-se que:
# 
# 1 pé =  12 polegadas;
# 1 jarda = 3 pés,
# 1 Milha = 1.760 jarda

#Entrada de dados:
pes = int( input('inserir o valor em pes:'))


#Processamento de dados:
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760


#Saida de dados:
print('polegadas:', polegadas)
print('jardas:' , jardas)
print('milhas:' , milhas )
