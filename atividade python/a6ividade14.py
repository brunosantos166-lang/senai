contador = 0
soma = 0 
média=soma/5
while contador < 5:
    salario = float (input (f"insira o {contador + 1} salario :"))
    soma +=salario
    contador += 1
    media = soma/5
print("a medida dos salarios é : " ,media)