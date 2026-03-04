maior = float()
menor =float()
soma = 0 
acima_100 =0
for cont in range(10):
    temperatura = float(input(f"digite a {cont +1} temperatura:"))
    soma += temperatura
    if cont == 0:
        maior = temperatura
    if temperatura > maior:

        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > 100 :
        acima_100 += 1
media = soma/10

print(f"a maior temperatura foi {maior}")
print(f"a menor temperatura foi {menor}")
print(f"a media das temperaturas foi {media}")
print(f"a temperatura ultrapassou 100°c {acima_100} vezes")

       
