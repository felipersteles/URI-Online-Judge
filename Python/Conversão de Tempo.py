"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""

num = int(input())

from math import floor
horas = floor(num/3600)
num = num % 3600

minutos = floor(num/60)
num = num % 60

segundos = num

print(horas,minutos,segundos,sep=":")
