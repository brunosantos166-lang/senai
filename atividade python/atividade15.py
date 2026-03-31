numero = int(input("Digite qual tabuada você quer ver: "))
print(f"\nTabuada do {numero}:\n")
for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}") j