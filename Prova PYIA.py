produtos = {}
qntd_produtos = int(input("\nDeseja inserir quantos produtos?: "))

for x in range(qntd_produtos):
    nome_produto = input(f"\nInsira o nome do produto {x+1}: ")
    valor_produto = float(input(f"\nInsira o valor do produto {x+1}:"))
    produtos[nome_produto] = valor_produto


valor_total = sum(produtos.values())

print(f"\nO valor total da compra é: R$ {valor_total:.2f}")
