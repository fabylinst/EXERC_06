import csv

with open('exemplo01.csv', 'r', newline='', encoding='utf-8') as arquivo:
    arquivo_lido = csv.reader(arquivo, delimiter=';')
    # print(arquivo_lido)

    for linha in arquivo_lido:
        print(arquivo_lido)
