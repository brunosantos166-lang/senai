estoque ={}
print("bem-vindo ao sistema de gestaõ de estoque desenvolvido por bruno bohnenberger")
while True:
   operaçao = input("deseja registrar a entrada e saida de produtos? (digete' entrada' ou 'saída')ou sair    ").lower()
   
   if operaçao not in ['entrada', 'saida', 'sair']:
      print("operaçao invalida")
      continue
   if operaçao =='sair': 
      break
   
   produto = input("nome do produto: ").strip()
   qtd = int(input("quantidade: "))

   if operaçao == 'entrada':
      estoque[produto] = estoque.get(produto,0) + qtd 
if operaçao == 'saida':
      if estoque.get(produto, 0) >= qtd:
        estoque[produto] -= qtd
      else:
         print("Erro:produto inexistente ou estoque insuficiente.")


print("\n ---Estoque final ---")
for p, q in estoque.items():
   print(f"{p}: {q}")