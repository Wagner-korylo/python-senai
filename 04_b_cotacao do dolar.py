#Autor: Wagner Korylo
#Data: 24//09/2024
#Descrição: Faça um algaritimo que um valor na moeda real ( R$ ),
#           a cotação da conversão REAL para DÓLAR,e  apresente
#           a quantiddade desse calor em dolar ( $ )
#           --------------------------------------------
#            Exemplo de execução
#            Insira o valor em real: 5000
#            Insira cotação do dia: 5
#            R$5000,00 equivalem $1000,00
#Entrada de dados:
moeda_real_string = input ('inserir o valor em R$:') 
cotacao_dia_string = input('Insira o valor da cotacao:')

#Processamento de dados:
moeda_real = int(moeda_real_string)
cotacao_dia = int(cotacao_dia_string)
moeda_dolar = moeda_real / cotacao_dia
#Saida de dados:
print(f'R$ {moeda_real} equivalem $ {moeda_dolar}') #format
print ('R$ ' + str(moeda_real) +' equivalem $' + str(moeda_dolar))
