"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
"""

horaini,minutoini,horafim,minutofim = input().split()

horaini = int(horaini)
horafim= int(horafim)
minutoini = int(minutoini)
minutofim = int(minutofim)

def ConverteHorarioemMinuto(hora,minuto):
    return hora*60 + minuto

inicio = ConverteHorarioemMinuto(horaini,minutoini)
fim = ConverteHorarioemMinuto(horafim,minutofim)
print('inicio e fim',inicio,fim)
    
tempoPartida = fim - inicio
    
if tempoPartida > 0:
    duracao = tempoPartida
else:
    duracao = 1440 + tempoPartida

horas = int(duracao/60)
minutos = duracao % 60

print('O JOGO DUROU',horas,'HORA(S) E',minutos,'MINUTO(S)')

