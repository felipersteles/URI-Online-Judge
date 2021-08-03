#Nao solucionado (tempo excedido)

"""
Marianne está criando um jogo chamado “Herói da Guitarra”. É um trabalho extremamente cansativo, que requer bastante empenho e tempo, mas nada que uma greve não resolva. Ao abrir o seu email, Mari se deparou com um problema bastante curioso proposto pelos primos Renè e Leonhard e pelos gêmeos Isaac e Carl.

O problema é descrito da seguinte forma:

“Um número natural é dito primo, se ele possui exatamente dois divisores naturais distintos: o número um e ele mesmo. Um número é dito primo gêmeo, se e somente se, ele for primo e houver outro número primo qualquer cuja diferença absoluta entre esse dois números primos seja igual a dois. Por exemplo, o número 3 é um primo gêmeo, pois ele é primo e existe outro primo (5) tal que |3 - 5| = 2, já o número 23, apesar de ser primo, não é um primo gêmeo. Você poderia nos dizer quantos número primos gêmeos existem entre x e y, inclusive?”

Marianne adora resolver esse tipo de problema, mas está muito ocupada criando o seu próprio jogo de Herói da Guitarra. Você pode ajudar?

Entrada
A primeira linha de entrada irá conter um inteiro 1 ≤ Q ≤ 105, o número de consultas, cada uma das próximas Q linhas irá contér dois inteiros, 1 ≤ X, Y ≤ 106.

Saída
Para cada uma das Q consultas, imprima a quantidade de número primos gêmeos entre X e Y, inclusive.
"""

def EhPrimo(num):
    if num%2 == 0 and num != 2 or num == 1:
        return False
    else:
        for i in range(3,num,2):
            if num%i == 0:
                return False
        
    return True

def EhPrimoGemeo(num):
    if EhPrimo(num) == True:
        if EhPrimo(num+2) == True or EhPrimo(num-2) == True:
            return True
    return False
    

Q = int(input())

cont = []

for i in range(Q):
    
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    aux = 0
    for j in range(x,y+1):
        if EhPrimoGemeo(j) == True:
            aux+=1
            
    cont.append(aux)
            
for i in range(len(cont)):
    print(cont[i])
            
