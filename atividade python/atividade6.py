nome =input("insira o nome:")
idade = int (input("insira a idade: "))

#repete quando a idade for valida
while idade > 120 or idade < 0:
    print = int(input("idade(anos comletos - ate 120)"))
dias_vida = idade * 365
print (f" {nome},voce viveu {dias_vida}")
