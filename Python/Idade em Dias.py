"""
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
"""

num = int(input())

from math import floor
if num >= 365:
    anos = floor(num/365)
    num -= 365*floor(num/365)
else:
    anos = 0

if num >= 30:
    meses = floor(num/30)
    num -= 30*floor(num/30)
else:
    meses = 0
    
if num < 30:
    dias = num
    num = 0
else:
    dias = 0
    
print(anos,'ano(s)')
print(meses,'mes(es)')
print(dias,'dia(s)')

#Não precisava dessa quantidade de if e bastava ter utilizado a operação resto(%)
