"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.
"""

x = -1
r = []
while x!=0 or y!=0:
    x,y = input().split()
    x = int(x)
    y = int(y)
    
    if x>0 and y>0:
        r.append('primeiro')
    elif x>0 and y<0:
        r.append('quarto')
    elif x<0 and y<0:
        r.append('terceiro')
    elif x<0 and y>0:
        r.append('segundo')
    else:
        break

for i in r:
    print(i)
    
    
