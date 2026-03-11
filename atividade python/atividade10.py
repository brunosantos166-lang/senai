soma = 0
acima_15 = 0
acima_20 = 0
acima_200 = 0
sobrecarga = False
alerta = range(8)
for i in range(8):
    corrente = float(input(f"digite a {i+1} mediçao decorrente (A):"))
    soma += corrente
 
    if corrente > 15:
        acima_15 += 1
    if corrente > 20:
        sobrecarga = True
        acima_20 +=1
    if corrente > 200:
        alerta = True
        acima_200 +=1
media = soma/ 8
print("mediçoes acima 15 (A)",acima_15)
print("media da corrente:",media)
if sobrecarga:
    print(F"huve sobrecarga no motor {acima_20} vezes")
if alerta:
    print(F"alerta: mediçao ultrapassou 200 {acima_200} vezes")
            