# Saulo Justiniano
# Unifip - Patos-PB
# Dia 05 de Março de 2020.

'''
2. Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros de água.
Sabendo que em 1 m3 de água há 1.000 litros, calcule quantos banhos de 5 minutos são necessários
para consumir 1 metro cúbico de água?
'''

consumo = float(input("Digite quantos litros de água gastar em 5 min: "))

total = 1000 / consumo

print(f"Em {total:.0f} banhos você gastará 1m³ de água")
